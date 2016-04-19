# coding=utf-8
from math import fabs, cos, sin


class Amino:
    id = -1
    x = -1

    def __init__(self, name, x=None, y=None):
        Amino.id += 1
        self.id = Amino.id
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
        return self.name == 'H' == other.name and fabs(self.x - other.x) <= 1 and fabs(self.y - other.y) <= 1

    def __repr__(self):
        return '[' + str(self.id) + ']' + self.name

    def rotate_relative(self, angle, other):
        sinn = sin(angle)
        coss = cos(angle)
        x = self.x - other.x
        y = self.y - other.y
        self.x = int(round(x * coss - y * sinn) + other.x)
        self.y = int(round(x * sinn + y * coss) + other.y)

    def to_pdb(self):
        section = 'ATOM'.ljust(6)  # 1-6
        id = str(self.id).rjust(5)  # 7-11
        space1 = ''.rjust(1)  # 12
        name = ' C'.ljust(4)  # 13-16
        altLoc = ''.rjust(1)  # 17
        if self.name == 'H':
            resName = 'ALA'.rjust(3)  # 18-20
        else:
            resName = 'ARG'.rjust(3)  # 18-20
        space2 = ''.rjust(1)  # 21
        chain = 'A'.rjust(1)  # 22
        resSeq = str(self.id).rjust(4)  # 23-26
        iCode = ''.rjust(1)  # 27
        space3 = ''.rjust(3)  # 28-30
        x = str(self.x).rjust(8)  # 31-38
        y = str(self.y).rjust(8)  # 39-46
        z = '0'.rjust(8)  # 47-54
        occupancy = ''.rjust(6)  # 55-60
        tempFactor = ''.rjust(6)  # 61-66
        space4 = ''.rjust(10)  # 67-76
        element = 'C'.rjust(2)  # 77-78
        charge = '0'.rjust(2)  # 79-80
        return section + id + space1 + name + altLoc + resName + space2 + chain + resSeq + iCode + space3 + x + y + z \
               + occupancy + tempFactor + space4 + element + charge
