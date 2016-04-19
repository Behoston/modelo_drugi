# coding=utf-8
from Amino import Amino
from Protein import Protein


class Sym:
    def __init__(self, sequence, steps=10000, temp_min=0.15, temp_max=1.0, temp_delta=0.05):
        self.protein = Protein([Amino(ch) for ch in sequence])
        self.steps = steps
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.temp_delta = temp_delta

    def run(self):
        temp = self.temp_max
        while temp > self.temp_min:
            for s in xrange(self.steps):
                move_accepted = False
                new_protein = self.protein.move(temp)
                if new_protein.is_valid():
                    if new_protein.get_energy() <= self.protein.get_energy():
                        self.protein = new_protein
                    else:
                        pass
            temp -= self.temp_delta
