def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("Text must be string")
    if color not in colors:
        raise ValueError("Value mismatched")
    if type(color) is not str:
        raise TypeError("Color must be in a string format")
    print(f"print {text} in {color}")


# print(colorize("hello", "yellow"))
print(colorize("hi", "str"))
