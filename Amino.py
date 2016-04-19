# coding=utf-8
from math import fabs


class Amino:
    id = -1
    x = -1

    def __init__(self, name, x=None, y=None):
        self.id = Amino.id
        Amino.id += 1
        self.name = name.upper()
        if x:
            self.x = x
        else:
            Amino.x += 1
            self.x = Amino.x
        if y:
            self.y = y
        else:
            self.y = 0

    def clash_with(self, other):
        return self.x == other.x and self.y == other.y

    def interact_with(self, other):
        return self.name == 'H' == other.type and fabs(self.x - other.x) <= 1 and fabs(self.y - other.y) <= 1

    def __repr__(self):
        return self.name
