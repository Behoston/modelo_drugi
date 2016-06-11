# coding=utf-8
from Sym import Sym
from drawing import draw_all

seqs = ['PHPPHPPHHPPHHPPHPPHP', 'HPPPHHPPHPHHHHHH', 'HPPPHHPPHPHHPHHH']

for seq in seqs:
    print seq

    simulation = Sym(seq)
    print '\tsimulation starting'
    simulation.run()
    print '\tsimulation done'

    print '\tdrawing'
    draw_all(seq)
    print '\tdrawing done'
