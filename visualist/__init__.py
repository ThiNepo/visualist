from PIL import Image, ImageDraw, ImageFont
import os 

CELL_SIZE = 32
SPACE = 16

font_path = os.path.join( os.path.abspath( os.path.dirname(__file__) ), 'fonts', 'Roboto-Medium.ttf' )
fnt = ImageFont.truetype(font_path, int(CELL_SIZE/2))

def draw_list(L,  highlight_indexes=[], color=(36, 116, 191, 255), highlight_color=(255, 46, 52, 255), indexes=True) -> Image:
    img = Image.new('RGBA', (320, 180), (255,255,255,255))
    MIDDLE = (img.size[0]/2, img.size[1]/2)

    draw = ImageDraw.Draw(img)
    begin = MIDDLE[0] - (len(L)/2)*(CELL_SIZE+SPACE) + SPACE/2
    
    for index, item in enumerate(L):
        X0 = begin
        X1 = begin + CELL_SIZE

        rect_color = color        
        if index in highlight_indexes:
            rect_color = highlight_color
        draw.rectangle([(X0, MIDDLE[1] - CELL_SIZE/2), 
                        (X1, MIDDLE[1] + CELL_SIZE/2)], fill=rect_color)

        text_size = draw.textsize(str(item), font=fnt)
        draw.text((begin + CELL_SIZE/2 - text_size[0]/2, 
                   MIDDLE[1] - CELL_SIZE/2 + text_size[1]/2), str(item), font=fnt)
            
        if indexes:
            text_size = draw.textsize(str(index), font=fnt)
            draw.text((begin + CELL_SIZE/2 - text_size[0]/2, 
                   MIDDLE[1] - CELL_SIZE - CELL_SIZE/2 + text_size[1]/2), 
                   str(index), 
                   font=fnt,
                   fill=(0,0,0,255))

        begin += CELL_SIZE+SPACE    

    return img

#img = draw_list([1, 2, -4, 2], [2])
#img.show()

