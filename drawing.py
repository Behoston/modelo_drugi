# coding=utf-8
import matplotlib.pyplot as plt


def draw_inertia(seq):
    inertia_file = open('output/' + seq + '/inertia.csv')
    inertia_temp = []
    inertia_value = []
    for line in inertia_file:
        l = line.strip().split(';')
        inertia_temp.append(l[0])
        inertia_value.append(l[1])
    inertia_file.close()
    plt.ylabel('inertia')
    plt.xlabel('temperature')
    plt.title('Inertia ' + seq)
    plt.grid(True)
    plt.plot(inertia_temp, inertia_value)
    plt.savefig('output/' + seq + '/inertia.png')
    plt.close()


def draw_heat(seq):
    heat_file = open('output/' + seq + '/heat.csv')
    heat_temp = []
    heat_value = []
    for line in heat_file:
        l = line.strip().split(';')
        heat_temp.append(l[0])
        heat_value.append(l[1])
    heat_file.close()
    plt.ylabel('heat')
    plt.xlabel('temperature')
    plt.title('Heat ' + seq)
    plt.grid(True)
    plt.colors()
    plt.plot(heat_temp, heat_value, color='red')
    plt.savefig('output/' + seq + '/heat.png')
    plt.close()


def draw_contact_histograms(seq):
    pass

#     temp = 1.0
#     while temp > 0:
#         contact_file = 'output/'+seq+
#
#         temp -= 0.05