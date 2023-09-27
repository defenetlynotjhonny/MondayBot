from datatreatment import prepost
import sys
from PIL import Image, ImageFont, ImageDraw 

content = prepost("MondayBot\PostDB.xlsx")
words = content.split()
distributor = len(words) // 4

for i in range(len(words)):
    if i % 4 and i > 4:
        words.insert(i, "\n")


content = ", ".join(words)
content = content.replace(",","")


image = Image.open('MondayBot\Images\Background.jpg')
draw = ImageDraw.Draw(image)


font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30)




center_horizontal = (image.getbbox()[0] + image.getbbox()[2]) // 2
center_vertical = (image.getbbox()[1] + image.getbbox()[3]) // 2
print(center_vertical,center_horizontal)
start_cords = (center_horizontal,center_vertical)

draw.multiline_text(start_cords, content, fill="Red", font=font, anchor="ms", spacing=4, align='center', direction=None, features=None, language=None, stroke_width=2, stroke_fill="yellow", embedded_color=False)
print(image.getbbox())
print(start_cords)
image.putpixel(start_cords,5)
image.show()
image.save("MondayBot\Images\copy.jpg")