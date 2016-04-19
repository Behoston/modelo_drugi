# coding=utf-8
from random import randint, choice

from Amino import Amino


class Protein:
    def __init__(self, sequence):
        self.energy = None
        self.sequence = sequence
        self.amino = [Amino(ch) for ch in sequence]
        self.length = len(sequence)

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

    def calculate_energy(self):
        self.energy = 0
        for i in xrange(self.length):
            for j in xrange(i + 2, self.length):
                if self.amino[i].interact_with(self.amino[j]):
                    self.energy -= 1

    def move(self):
        relative_amino_number = randint(1, self.length - 1)
        angle = choice([1.5707963267948966, 3.141592653589793, 4.71238898038469])
        for a in self.amino[relative_amino_number + 1:]:
            a.rotate_relative(angle, self.amino[relative_amino_number])
        self.calculate_energy()

    def __repr__(self):
        return 'Protein(' + str(self.amino) + ')'

    def to_pdb(self, ident):
        result = 'MODEL     ' + str(ident) + '\n'
        for a in self.amino:
            result += a.to_pdb() + '\n'
        result += 'ENDMDL\n'
        return result
