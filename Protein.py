# coding=utf-8
from math import radians
from random import randint, choice

from Amino import Amino


class Protein:
    def __init__(self, sequence):
        self.energy = None
        self.sequence = sequence
        self.amino = [Amino(ch) for ch in sequence]
        self.length = len(sequence)
        self.mass_center = None

    def is_valid(self):
        for i in xrange(self.length):
            for j in xrange(i + 1, self.length):
                if self.amino[i].clash_with(self.amino[j]):
                    return False
        return True

    def get_energy(self):
        if not self.energy:
            self.calculate_energy()
        return self.energy

    def get_mass_center(self):
        if not self.mass_center:
            self.calculate_mass_center()
        return self.mass_center

    def calculate_energy(self):
        self.energy = 0
        for i in xrange(self.length):
            for j in xrange(i + 2, self.length):
                if self.amino[i].interact_with(self.amino[j]):
                    self.energy -= 1

    def move(self):
        relative_amino_number = randint(1, self.length - 2)
        angle = choice([90, 180, 270])
        for a in self.amino[relative_amino_number + 1:]:
            a.rotate_relative(radians(angle), self.amino[relative_amino_number])
        self.recalculate()

    def recalculate(self):
        if self.energy:
            self.calculate_energy()
        if self.mass_center:
            self.calculate_mass_center()

    def __repr__(self):
        return 'Protein(' + str(self.amino) + ')'

    def to_pdb(self, ident):
        result = 'MODEL     ' + str(ident) + '\n'
        for a in self.amino:
            result += a.to_pdb() + '\n'
        result += 'ENDMDL\n'
        return result

    def calculate_mass_center(self):
        x = 0.0
        y = 0.0
        for a in self.amino:
            x += a.x
            y += a.y
        self.mass_center = (x / self.length, y / self.length)
        return self.mass_center

    def calculate_moment_of_inertia(self):
        result = 0
        for a in self.amino:
            result += (self.get_mass_center()[0] - a.x) ** 2 + (self.get_mass_center()[1] - a.y) ** 2
        return result
