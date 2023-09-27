from datatreatment import prepost
import sys
from PIL import Image, ImageFont, ImageDraw 
content = prepost("MondayBot\PostDB.xlsx")


# creating a image object
image = Image.open('MondayBot\Images\Background.jpg')

draw = ImageDraw.Draw(image)

# specified font size
font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30)


# drawing text size
draw.text((5, 5), content, font = font, align ="center")
#ImageDraw.multiline_text((50,50), content, fill="Red", font=None, anchor=None, spacing=4, align='center', direction=None, features=None, language=None, stroke_width=2, stroke_fill="yellow", embedded_color=False)

image.show()
image.save("copy.jpg")