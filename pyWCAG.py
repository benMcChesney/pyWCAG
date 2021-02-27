

'''
https://www.w3.org/TR/WCAG/#dfn-relative-luminance

For the sRGB colorspace, the relative luminance of a color is defined as
 L = 0.2126 * R + 0.7152 * G + 0.0722 * B where R, G and B are defined as:

if RsRGB <= 0.03928 then R = RsRGB/12.92 else R = ((RsRGB+0.055)/1.055) ^ 2.4
if GsRGB <= 0.03928 then G = GsRGB/12.92 else G = ((GsRGB+0.055)/1.055) ^ 2.4
if BsRGB <= 0.03928 then B = BsRGB/12.92 else B = ((BsRGB+0.055)/1.055) ^ 2.4
and RsRGB, GsRGB, and BsRGB are defined as:

RsRGB = R8bit/255
GsRGB = G8bit/255
BsRGB = B8bit/255
'''


def get_color_struct( _r, _g , _b ):
    color = {
        "r": _r 
        , "g" : _g
        , "b" : _b 
    }

    return color

def adjust_channel_for_colorspace( c ):
    
    adjusted_c  = c / 12.92
    if c > 0.03928 :
        adjusted_c = pow((c+0.055)/1.055 , 2.4 )
    return adjusted_c

# https://www.w3.org/TR/WCAG/#dfn-relative-luminance

def get_luminance( color, space = 'sRGB' ):

    print('debugger')
    rs_rgb = color['r'] / 255.0
    gs_rgb = color['g'] / 255.0
    bs_rgb = color['b'] / 255.0

    r = adjust_channel_for_colorspace( rs_rgb )
    g = adjust_channel_for_colorspace( gs_rgb )
    b = adjust_channel_for_colorspace( bs_rgb )

    luminance =  0.2126 * r + 0.7152 * g + 0.0722 * b
    return luminance


def get_contrast_ratio( col1, col2 ):

    col1_lum = get_luminance( col1 )
    col2_lum = get_luminance( col2 )

    l1 = col1_lum 
    l2 = col2_lum
    if ( l2 > l1 ):
        l1 = col2_lum
        l2 = col1_lum   

    contrast = ( l1 + 0.05 ) / ( l2 + 0.05 ) 
    return contrast
    # https://www.w3.org/TR/WCAG/#dfn-contrast-ratio
    # (L1 + 0.05) / (L2 + 0.05),