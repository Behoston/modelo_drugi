# coding=utf-8
from copy import deepcopy
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
        self.best = None

    def accept_higher_energy(self, new_protein):
        def pi(j):
            kb = 1
            return exp(-j / (kb * self.temp))

        return random() < (pi(new_protein.get_energy()) / pi(self.protein.get_energy()))

    def run(self):
        self.temp = self.temp_max
        all_steps = 0
        # clear file
        open('output/' + self.protein.sequence + '_trajectory.pdb', 'w').close()
        heat_stats_file = open('output/' + self.protein.sequence + '_heat.csv', 'w')
        contacts_stats_file = open('output/' + self.protein.sequence + '_contacts.csv', 'w')
        inertia_stats_file = open('output/' + self.protein.sequence + '_inertia.csv', 'w')
        while self.temp > self.temp_min:
            E2 = 0.0
            E = 0.0
            inertia_sum = 0.0
            contacts_stats_file.write(str(self.temp))
            inertia_stats_file.write(str(self.temp))
            for s in xrange(self.steps):
                all_steps += 1
                new_protein = deepcopy(self.protein)
                new_protein.move()
                if new_protein.is_valid():
                    if new_protein.get_energy() <= self.protein.get_energy():
                        self.protein = new_protein
                        self.best = new_protein
                    elif self.accept_higher_energy(new_protein):
                        self.protein = new_protein
                # stats
                contacts_stats_file.write(';' + str(-self.protein.get_energy()))
                inertia_sum += self.protein.calculate_moment_of_inertia()
                E2 += self.protein.energy ** 2
                E += self.protein.energy
                if all_steps % self.save_interval == 0:
                    with open('output/' + self.protein.sequence + '_trajectory.pdb', 'a') as f:
                        f.write(self.protein.to_pdb(all_steps / self.save_interval))
            inertia_stats_file.write(str(inertia_sum / self.steps))
            heat_stats_file.write(
                str(self.temp) + ';' + str(((E2 / self.steps) - (E / self.steps) ** 2) / self.temp ** 2) + '\n')
            contacts_stats_file.write('\n')
            inertia_stats_file.write('\n')
            self.temp -= self.temp_delta
        contacts_stats_file.close()
        inertia_stats_file.close()
        heat_stats_file.close()
        with open('output/' + self.protein.sequence + '_best.pdb', 'w') as f:
            f.write(self.best.to_pdb(0))
