import pyWCAG 

color1 = pyWCAG.get_color_struct( 35, 10, 0 )
color2 = pyWCAG.get_color_struct( 255, 123, 123 )

c = pyWCAG.get_contrast_ratio( color1, color2 )
print('contrast is', c )