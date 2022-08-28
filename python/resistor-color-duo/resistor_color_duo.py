RESISTOR_COLOR_VALUE = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}
def value(colors):
    resistence = ''
    for item in colors:
        resistence += str(color_code(item)) # no futuro tentar fazer o mesmo código usando matemática e não convertando para strings
    resistence = resistence[:2]
    return int(resistence)

def color_code(color):
    return RESISTOR_COLOR_VALUE[color]

