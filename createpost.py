from datatreatment import prepost
import sys
from PIL import Image, ImageFont, ImageDraw 
from stringbuilder import stringbuilder



def create_post():

    content = prepost("MondayBot\PostDB.xlsx")
    content = stringbuilder(content,4)


    image = Image.open('MondayBot\Images\Background.jpg')
    draw = ImageDraw.Draw(image)


    font = ImageFont.truetype(r'MondayBot\Fonds\Orena solo mayusculas.ttf', 50)




    center_horizontal = (image.getbbox()[0] + image.getbbox()[2]) // 2
    center_vertical = (image.getbbox()[1] + image.getbbox()[3]) // 2

    start_cords = (center_horizontal,center_vertical)

    draw.multiline_text(start_cords, content, fill="Green", font=font, anchor="mm", spacing=40, align='center', direction=None, features=None, language=None, stroke_width=5, stroke_fill="yellow", embedded_color=False)


    image.putpixel(start_cords,5)
    image.show()
    image.save("MondayBot\Images\copy.jpg")

create_post()