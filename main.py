# coding=utf-8
from Sym import Sym
from drawing import draw_inertia, draw_heat, draw_contact_histograms

seqs = ['PHPPHPPHHPPHHPPHPPHP', 'HPPPHHPPHPHHHHHH', 'HPPPHHPPHPHHPHHH']

for seq in seqs:
    print seq
    simulation = Sym(seq)
    print '\tsimulation starting'
    simulation.run()
    print '\tsimulation done'

    print '\tdrawing'
    draw_inertia(seq)
    draw_heat(seq)
    draw_contact_histograms(seq)
    print '\tdrawing done'
