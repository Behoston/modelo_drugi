# coding=utf-8
from Amino import Amino
from Protein import Protein


def run(s):
    protein = Protein([Amino(ch) for ch in s])
    print protein
    print 'Is valid:\t', protein.is_valid()
    print 'Energy:\t\t', protein.get_energy()


run('hphhhppphphphp')
