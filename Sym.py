# coding=utf-8
from copy import deepcopy

from Amino import Amino
from Protein import Protein
from math import exp
from random import random


class Sym:
    def __init__(self, sequence, steps=10000, temp_min=0.15, temp_max=1.0, temp_delta=0.05, save_interval=100):
        self.protein = Protein(sequence)
        self.steps = steps
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.temp_delta = temp_delta
        self.temp = temp_max
        self.save_interval = save_interval

    def accept_higher_energy(self, new_protein):
        def pi(j):
            kb = 1
            return exp(-j / (kb * self.temp))

        return random() < (pi(new_protein.get_energy()) / pi(self.protein.get_energy()))

    def run(self):
        self.temp = self.temp_max
        all_steps = 0
        while self.temp > self.temp_min:
            for s in xrange(self.steps):
                all_steps += 1
                new_protein = deepcopy(self.protein)
                new_protein.move()
                if new_protein.is_valid():
                    if new_protein.get_energy() <= self.protein.get_energy():
                        self.protein = new_protein
                    elif self.accept_higher_energy(new_protein):
                        self.protein = new_protein
                    if all_steps % self.save_interval == 0:
                        with open('output/' + self.protein.sequence + '.pdb', 'a') as f:
                            f.write(self.protein.to_pdb(all_steps / self.save_interval))
            self.temp -= self.temp_delta
