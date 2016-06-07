# coding=utf-8
import os
from copy import deepcopy
from Protein import Protein
from math import exp
from random import random


class Sym:
    def __init__(self, sequence, steps=10000, temp_min=0.15, temp_max=1.0,
                 temp_delta=0.05, save_interval=100):
        self.protein = Protein(sequence)
        self.steps = steps
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.temp_delta = temp_delta
        self.temp = temp_max
        self.save_interval = save_interval
        self.best = None

    def accept_higher_energy(self):
        def pi(j):
            kb = 1.0
            return exp(-j / (kb * self.temp))

        return random() < (pi(self.protein.energy) / pi(self.protein.last_energy))

    def run(self):
        try:
            os.makedirs('output/' + self.protein.sequence)
        except:
            # directory exists?
            pass
        self.temp = self.temp_max
        global_steps_done = 0
        # clear file
        open('output/' + self.protein.sequence + '/trajectory.pdb', 'w').close()
        heat_stats_file = open('output/' + self.protein.sequence + '/heat.csv',
                               'w')
        contacts_stats_file = open(
            'output/' + self.protein.sequence + '/contacts.csv', 'w')
        inertia_stats_file = open(
            'output/' + self.protein.sequence + '/inertia.csv', 'w')
        while self.temp >= self.temp_min:
            E2 = 0.0
            E = 0.0
            inertia_sum = 0.0
            best_for_temperature = None
            contacts_stats_file.write(str(self.temp))
            inertia_stats_file.write(str(self.temp))
            for s in xrange(self.steps):
                global_steps_done += 1
                # new_protein = deepcopy(self.protein)
                self.protein.move()
                if self.protein.is_valid():
                    if self.protein.energy <= self.protein.last_energy:
                        pass
                    elif self.accept_higher_energy():
                        pass
                    else:
                        self.protein.undo_move()
                else:
                    self.protein.undo_move()
                # saving best model
                if self.best is None:
                    self.best = deepcopy(self.protein)
                elif self.protein.energy < self.best.energy:
                    self.best = deepcopy(self.protein)
                # best for actual temperature
                if best_for_temperature is None:
                    best_for_temperature = deepcopy(self.protein)
                elif self.protein.energy < best_for_temperature.energy:
                    best_for_temperature = deepcopy(self.protein)
                # stats
                contacts_stats_file.write(';' + str(-self.protein.energy))
                inertia_sum += self.protein.calculate_moment_of_inertia()
                E2 += self.protein.energy ** 2
                E += self.protein.energy
                self.save_trajectory(global_steps_done)
            self.save_best_for_actual_temp(best_for_temperature)
            inertia_stats_file.write(';' + str(inertia_sum / self.steps) + '\n')
            E /= self.steps
            E2 /= self.steps
            heat_stats_file.write(str(self.temp) + ';' + str(
                (E2 - E ** 2) / self.temp ** 2) + '\n')
            contacts_stats_file.write('\n')
            self.temp -= self.temp_delta
        contacts_stats_file.close()
        inertia_stats_file.close()
        heat_stats_file.close()
        self.save_best()

    def save_best_for_actual_temp(self, best_for_temperature):
        with open('output/' + self.protein.sequence + '/best_for_' + str(
                self.temp) + '.pdb', 'w') as f:
            f.write(best_for_temperature.to_pdb(self.temp))

    def save_best(self):
        with open('output/' + self.protein.sequence + '/best.pdb', 'w') as f:
            f.write(self.best.to_pdb(0))

    def save_trajectory(self, all_steps):
        if all_steps % self.save_interval == 0:
            with open('output/' + self.protein.sequence + '/trajectory.pdb',
                      'a') as f:
                f.write(self.protein.to_pdb(all_steps / self.save_interval))
