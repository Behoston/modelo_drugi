# coding=utf-8
from math import radians
from random import randint, choice

from Amino import Amino


class Protein(object):
    def __init__(self, sequence):
        self.sequence = sequence
        self.amino = [Amino(ch) for ch in sequence]
        self.length = len(sequence)
        self.energy = None
        self.calculate_energy()
        self.mass_center = None
        self.calculate_mass_center()

        self.last_rotation_degree = None
        self.last_resid_to_move = None
        self.last_mass_center = None
        self.last_energy = None

    def is_valid(self):
        for i in xrange(self.length):
            for j in xrange(i + 1, self.length):
                if self.amino[i].clash_with(self.amino[j]):
                    return False
        return True

    def calculate_energy(self):
        self.energy = 0
        for i in xrange(self.length):
            for j in xrange(i + 2, self.length):
                if self.amino[i].interact_with(self.amino[j]):
                    self.energy -= 1

    def move(self):
        self.last_resid_to_move = randint(1, self.length - 2)
        self.last_rotation_degree = choice([90, 180, 270])
        self.last_energy = self.energy
        self.last_mass_center = self.mass_center
        for a in self.amino[self.last_resid_to_move + 1:]:
            a.rotate_relative(radians(self.last_rotation_degree),
                              self.amino[self.last_resid_to_move])
        self.recalculate()

    def undo_move(self):
        for a in self.amino[self.last_resid_to_move + 1:]:
            a.rotate_relative(radians(-self.last_rotation_degree),
                              self.amino[self.last_resid_to_move])
        self.energy = self.last_energy
        self.last_energy = None
        self.mass_center = self.last_mass_center
        self.last_mass_center = None

    def recalculate(self):
        self.calculate_energy()
        self.calculate_mass_center()

    def __repr__(self):
        return 'Protein(' + str(self.amino) + ')'

    def __eq__(self, other):
        if not isinstance(other, Protein):
            return False
        energy = self.energy == other.energy
        mass_center = self.mass_center == other.mass_center
        sequence = self.sequence == other.sequence
        length = self.length == other.length
        amino = self.amino == other.amino
        return energy and mass_center and sequence and length and amino

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
            result += (self.mass_center[0] - a.x) ** 2 + \
                      (self.mass_center[1] - a.y) ** 2  # ** 0.5 ** 2
        return result
