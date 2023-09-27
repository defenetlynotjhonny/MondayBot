from datatreatment import prepost
import sys
from PIL import Image, ImageFont, ImageDraw 

content = prepost("MondayBot\PostDB.xlsx")
print(len(content))
words = content.split()
print("Teste", words)
print(len(words))

distributor = len(words) // 4
for i in range(len(words)):
    if i % 4 and i > 4:
        words.insert(i, "\n")

print("Treated: " , words)
content = ", ".join(words)
content = content.replace(",","")
print(content)
# creating a image object
image = Image.open('MondayBot\Images\Background.jpg')

draw = ImageDraw.Draw(image)

# specified font size
font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30)


# drawing text size
#draw.text((50,50), content, fill="Red", font=font, anchor=None, spacing=0, align='center', direction=None, features=None, language=None, stroke_width=2, stroke_fill="yellow", embedded_color=False)
draw.multiline_text((50,50), content, fill="Red", font=font, anchor=None, spacing=4, align='center', direction=None, features=None, language=None, stroke_width=2, stroke_fill="yellow", embedded_color=False)

image.show()
image.save("copy.jpg")