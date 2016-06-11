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
    plt.plot(heat_temp, heat_value, color='red')
    plt.savefig('output/' + seq + '/heat.png')
    plt.close()


def draw_contact_histograms(seq):
    with open('output/' + seq + '/contacts.csv') as contacts_file:
        for line in contacts_file:
            line = line.strip().split(';')
            temp = line[0]
            if len(temp) == 3:
                temp += '0'
            values = [int(i) for i in line[1:]]
            plt.title('Contacts for ' + seq + ' for ' + temp)
            plt.xlabel('contacts')
            plt.ylabel('quantity')
            plt.hist(values, range=(0, len(seq) / 2), normed=False,
                     color='green')
            plt.savefig('output/' + seq + '/contacts_' + temp + '.png')
            plt.close()


def draw_all(seq):
    draw_heat(seq)
    draw_inertia(seq)
    draw_contact_histograms(seq)
