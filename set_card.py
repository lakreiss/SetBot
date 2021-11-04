from enum import Enum
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

class Shape(Enum):
    DIAMOND = 1
    SQUIGGLE = 2
    OVAL = 3

class Shade(Enum):
    EMPTY = 1
    STRIPED = 2
    FULL = 3

class Color(Enum):
    PURPLE = 1
    RED = 2
    GREEN = 3

class SetCard():
    def __init__(self, *args):
        if len(args) == 6:
            self.create_card_from_site(args)
        elif len(args) == 1:
            print(args)
            split_string = list(args[0])
            print(split_string)
            self.create_card_from_text(split_string[0], split_string[1], split_string[2], split_string[3])

    def create_card_from_site(self, args):
        self.parent = args[0]
        self.number = self.get_number(args[1])
        self.shape = self.get_shape(args[2])
        self.shade = self.get_shade(args[3], args[4])
        self.color = self.get_color(args[5])
    
    def create_card_from_text(self, *args):
        self.number = self.get_number(int(args[0]))
        self.shape = self.get_shape(args[1])
        self.shade = self.get_shade(args[2])
        self.color = self.get_color(args[3])

    def get_number(self, number):
        if (number == 1):
            return Number.ONE
        elif (number == 2):
            return Number.TWO
        elif (number == 3):
            return Number.THREE
        else:
            raise Exception("Illegal card number")

    def get_shape(self, value):
        if (value == '#oval' or value == 'o'):
            return Shape.OVAL
        elif (value == '#squiggle' or value == 's'):
            return Shape.SQUIGGLE
        elif (value == '#diamond' or value == 'd'):
            return Shape.DIAMOND
        else:
            raise Exception("Illegal card shape")

    def get_shade(self, *args):
        if len(args) == 2:
            mask = args[0]
            fill = args[1]
            if mask == 'url(#mask-stripe)':
                return Shade.STRIPED
            elif fill == 'transparent':
                return Shade.EMPTY
            else:
                return Shade.FULL
        elif len(args) == 1:
            shade_letter = args[0]
            print(shade_letter)
            if shade_letter == 's':
                return Shade.STRIPED
            elif shade_letter == 'e':
                return Shade.EMPTY
            elif shade_letter == 'f':
                return Shade.FULL
            else:
                raise Exception("Illegal card shade")

    
    def get_color(self, value):
        if value == '#800080' or value == 'p':
            return Color.PURPLE
        elif value == '#ff0101' or value == 'r':
            return Color.RED
        elif value == '#008002' or value == 'g':
            return Color.GREEN
        else:
            raise Exception("Illegal card color")

    def __str__(self):
        return "Number: {number} Color: {color} Shape: {shape} Shade: {shade}\n".format(number=self.number, color=self.color, shape=self.shape, shade=self.shade)