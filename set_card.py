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
    def __init__(self, parent, number, href, mask, fill, hex_color):
        self.parent = parent
        self.number = self.get_number(number)
        self.shape = self.get_shape(href)
        self.shade = self.get_shade(mask, fill)
        self.color = self.get_color(hex_color)

    def get_number(self, number):
        if (number == 1):
            return Number.ONE
        elif (number == 2):
            return Number.TWO
        elif (number == 3):
            return Number.THREE
        else:
            raise Exception("Illegal card number")

    def get_shape(self, href):
        if (href == '#oval'):
            return Shape.OVAL
        elif (href == '#squiggle'):
            return Shape.SQUIGGLE
        elif (href == '#diamond'):
            return Shape.DIAMOND
        else:
            raise Exception("Illegal card shape")

    def get_shade(self, mask, fill):
        if mask == 'url(#mask-stripe)':
            return Shade.STRIPED
        elif fill == 'transparent':
            return Shade.EMPTY
        else:
            return Shade.FULL
    
    def get_color(self, hex_color):
        if hex_color == '#800080':
            return Color.PURPLE
        elif hex_color == '#ff0101':
            return Color.RED
        elif hex_color == '#008002':
            return Color.GREEN
        else:
            raise Exception("Illegal card color")

    def __str__(self):
        return "Parent: {parent}\nNumber: {number} Color: {color} Shape: {shape} Shade: {shade}\n".format(parent=self.parent, number=self.number, color=self.color, shape=self.shape, shade=self.shade)