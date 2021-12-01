import numpy as np
import ajuste
import plotgraf
# Leitura de dados
ifile = "reduzido.txt"
x, y, erro = np.loadtxt(ifile, dtype=float).transpose()


#linearizacao

H = np.power(x, 0.5)
a0, a1 = ajuste.reta(H, y)
g = 2/np.power(a1,2)
plotgraf.grafico(x, y, erro, g)
