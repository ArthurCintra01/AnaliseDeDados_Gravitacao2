import matplotlib.pylab as plt
import math
import numpy as np

def funcaogravidade(alt):
    return math.sqrt((2*alt)/9.81)

def grafico(x,y,erro,g):
    # grafico
    plt.errorbar(x, y, yerr=erro, fmt="ro", label="Dados")
    xx = np.linspace(0.5, 2.5, 1000)
    yy = np.power(2 * xx, 0.5) * np.power(1 / g, 0.5)
    plt.plot(xx, yy, label="g={:.2f}".format(g))
    # plot curva tempo com g=9.81
    alt = np.linspace(0.5, 2.5, 1000)
    med = np.zeros(len(alt))
    for i in range(len(med)):
        med[i] = funcaogravidade(alt[i])
    plt.plot(alt, med, label="g=9.81")
    plt.xlabel("Altura(m)")
    plt.ylabel("Tempo(s)")
    plt.margins(0.5)
    plt.legend()
    plt.grid()
    plt.show()
