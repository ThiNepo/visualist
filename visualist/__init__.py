from PIL import Image, ImageDraw, ImageFont
import os 


class Visualist:

    def __init__(self, image_size, cell_size=32, space=16):
        self.IMAGE_SIZE = image_size
        self.CELL_SIZE = cell_size
        self.SPACE = space

        font_path = os.path.join( os.path.abspath( os.path.dirname(__file__) ), 'fonts', 'Roboto-Medium.ttf' )
        self.font = ImageFont.truetype(font_path, int(self.CELL_SIZE/2))

    def img_from_list(self, L, highlight_indexes=[], color=(36, 116, 191, 255), highlight_color=(255, 46, 52, 255), indexes=True) -> Image:

        img = Image.new('RGBA', self.IMAGE_SIZE, (255,255,255,255))
        MIDDLE = (img.size[0]/2, img.size[1]/2)

        draw = ImageDraw.Draw(img)
        pointer = MIDDLE[0] - (len(L)/2)*(self.CELL_SIZE+self.SPACE) + self.SPACE/2
        
        for index, item in enumerate(L):
            X0 = pointer
            X1 = pointer + self.CELL_SIZE

            rect_color = color        
            if index in highlight_indexes:
                rect_color = highlight_color
            draw.rectangle([(X0, MIDDLE[1] - self.CELL_SIZE/2), 
                            (X1, MIDDLE[1] + self.CELL_SIZE/2)], fill=rect_color)

            text_size = draw.textsize(str(item), font=self.font)
            draw.text((pointer + self.CELL_SIZE/2 - text_size[0]/2, 
                    MIDDLE[1] - self.CELL_SIZE/2 + text_size[1]/2), str(item), font=self.font)
                
            if indexes:
                text_size = draw.textsize(str(index), font=self.font)
                draw.text((pointer + self.CELL_SIZE/2 - text_size[0]/2, 
                    MIDDLE[1] - self.CELL_SIZE - self.CELL_SIZE/2 + text_size[1]/2), 
                    str(index), 
                    font=self.font,
                    fill=(0,0,0,255))

            pointer += self.CELL_SIZE + self.SPACE    

        return img

#img = draw_list([1, 2, -4, 2], [2])
#img.show()

