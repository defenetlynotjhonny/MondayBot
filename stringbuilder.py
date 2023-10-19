

def stringbuilder(string, x=4):
    words = string.split()
    result = ''
    for i, word in enumerate(words):
        result += word
        if (i + 1) % x == 0:
            result += '\n'
        else:
            result += ' '
    return result

def text_wrap(text, font, max_width=700):
    textlen = font.getlength(text)
    words = text.split()
    current = " "
    result = []
    for word in words:
        if font.getlength(current) + font.getlength(word) < max_width:
            result.append(word)
            current = current + "  " + word
        else:
            result.append( "\n" +  word )
            current = " " 
            

    text = "  ".join(result)
    print(result)
    return text

