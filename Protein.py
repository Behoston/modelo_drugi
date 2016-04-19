# coding=utf-8


class Protein:
    def __init__(self, amino):
        self.energy = None
        self.amino = amino
        self.length = len(amino)

    def is_valid(self):
        for i in xrange(self.length):
            for j in xrange(i + 1, self.length):
                if self.amino[i].clash_with(self.amino[j]):
                    return False
        return True

    def get_energy(self):
        if not self.energy:
            self.energy = 0
            for i in xrange(self.length):
                for j in xrange(i + 2, self.length):
                    if self.amino[i].interact_with(self.amino[j]):
                        self.energy -= 1
        return self.energy

    def move(self, temp):
        pass

    def __repr__(self):
        return 'Protein(' + str(self.amino) + ')'
