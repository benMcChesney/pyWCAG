import pyWCAG 
import sys
import json
import pandas as pd 
import os
import os.path
from json.decoder import JSONDecodeError

config = "" 
args = sys.argv

if len(args) >= 2 :
    path = os.path.join( os.getcwd(), args[1] )
    with open(path , 'r' ) as f:
        config = json.loads( f.read() )

print( f"parsing theme {config['name']} ")
colors = config['dataColors']

rows = [] 
# dataColors defines the palette. Table Accent doesn't act as a background.
ignore_attribs = [ "dataColors" , "tableAccent" ]
filter_attribs = [ "foreground" ] 
color_index = 0 
for c_hex in colors :

    #if color_index >= 6 : 
    #    break 
    c = pyWCAG.hex_to_rgb_color( c_hex )
    for attrib in config :  
        if attrib not in ignore_attribs :
            attrib_hex = config[attrib] 
            if attrib_hex.find( "#" ) >= 0 :
                attrib_color = pyWCAG.hex_to_rgb_color( attrib_hex )
                score = pyWCAG.get_contrast_ratio( c , attrib_color )
                print ( f"testing {attrib}({attrib_hex}) with { c_hex } = {score} ")
                row = {
                    "theme_color" : c_hex.upper() , 
                    "attrib_color" : attrib_hex.upper() , 
                    "attrib_name" : attrib , 
                    "wcag_score" : score ,
                    "color_index" : color_index
                }
                rows.append( row ) 
    color_index += 1 

df = pd.DataFrame( rows )
p =  './wcag_pbi_theme_results.csv' 
df.to_csv( p , index=False )
print( f'results exported to {p}')
#c = pyWCAG.get_contrast_ratio( color1, color2 )
#print('contrast is', c )