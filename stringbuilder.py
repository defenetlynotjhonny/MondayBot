

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

