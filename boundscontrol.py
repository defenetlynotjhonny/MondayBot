from PIL import Image, ImageDraw, ImageFont


def draw_text_with_bounds(text, font_path, max_width, max_height):
    # Create a blank image with a white background
    image = Image.open('Images\Background.jpg')
    draw = ImageDraw.Draw(image)

    # Load a TrueType font
    font_size = 18
    font = ImageFont.truetype(r'Fonds\Orena solo mayusculas.ttf', 45)

    # Split the input text into lines based on word wrapping
    lines = []
    words = text.split()
    current_line = ''
    
    for word in words:
        test_line = current_line + (word + ' ' if current_line else word)
        text_width, text_height = draw.textsize(test_line, font)
        
        if text_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
    
    if current_line:
        lines.append(current_line)

    # Calculate the total text height
    total_text_height = len(lines) * text_height

    # Calculate the vertical centering position
    vertical_position = (max_height - total_text_height) // 2

    # Draw the text on the image with proper position and line breaks
    for line in lines:
        text_width, text_height = draw.textsize(line, font)
        horizontal_position = (max_width - text_width) // 2
        draw.text((horizontal_position, vertical_position), line, font=font, fill='black')
        vertical_position += text_height

    return image

# Example usage:
input_text = "This is an example of text that should not go out of bounds in the image."
font_path = "path_to_your_font_file.ttf"  # Replace with the path to your TTF font file
max_width = 400  # Maximum width for the image
max_height = 300  # Maximum height for the image

image = draw_text_with_bounds(input_text, font_path, max_width, max_height)
image.show()
