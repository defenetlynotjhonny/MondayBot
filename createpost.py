from datatreatment import prepost
import sys
from PIL import Image, ImageFont, ImageDraw 
from stringbuilder import stringbuilder, text_wrap

longteststring = " sans publicité, et sans recourir à lexploitation des données personnelles de ses utilisateurs.es rédacteurs des articles de Wikipédia sont bénévoles. Ils coordonnent leurs efforts au sein dune communauté collaborative, sans dirigeant. "





def create_post():

    content = prepost("PostDB.xlsx")
    
    #content = stringbuilder(content,4)


    image = Image.open('Images\Background.jpg')
    draw = ImageDraw.Draw(image)

    fontsize = 45
    font = ImageFont.truetype(r'Fonds\Hexa.ttf', fontsize)
    content = text_wrap(content,font)
    
    print(font.getlength(content))
    print(text_wrap(content,font,1080))
    


    center_horizontal = (image.getbbox()[0] + image.getbbox()[2]) // 2
    center_vertical = (image.getbbox()[1] + image.getbbox()[3]) // 2

    start_cords = (center_horizontal,center_vertical)

    draw.multiline_text(start_cords, content, fill="Green", font=font, anchor="mm", spacing=40, align='center', direction=None, features=None, language=None, stroke_width=5, stroke_fill="yellow", embedded_color=False)


    image.putpixel(start_cords,5)
    image.show()
    image.save("Images\copy.jpg")

create_post()









