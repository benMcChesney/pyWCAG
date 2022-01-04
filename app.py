import pyWCAG 
import sys


color1 = ""
color2 = "" 

args = sys.argv
if len(args) >= 3 :
    c1_hex = args[1] #"#FFFFFF"
    c2_hex = args[2] #"#FFCCAA"
    color1 = pyWCAG.hex_to_rgb_color( c1_hex )
    color2 = pyWCAG.hex_to_rgb_color( c2_hex ) 

else : 
    print ( 'using default values, no args detected')
    color1 = pyWCAG.get_color_struct( 35, 10, 0 )
    color2 = pyWCAG.get_color_struct( 255, 123, 123 )

c = pyWCAG.get_contrast_ratio( color1, color2 )
print('contrast is', c )