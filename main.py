# coding=utf-8
from Sym import Sym
from drawing import draw_inertia, draw_heat, draw_contact_histograms
import matplotlib.pyplot as plt

seqs = ['PHPPHPPHHPPHHPPHPPHP', 'HPPPHHPPHPHHHHHH', 'HPPPHHPPHPHHPHHH']
# seqs = ['HHHPPP']

for seq in seqs:
    simulation = Sym(seq)
    simulation.run()
    print seq

    # drawing
    draw_inertia(seq)
    draw_heat(seq)
    draw_contact_histograms(seq)
