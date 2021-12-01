def reta(x,y):
  n = len(x)
  assert len(y)==n, "x e y têm tamanhos diferentes"

  somax  = 0
  somax2 = 0
  somay  = 0
  somaxy = 0
  for i in range(n):
    somax  += x[i]
    somax2 += x[i]*x[i]
    somay  += y[i]
    somaxy += x[i]*y[i]

  den = n*somax2 - somax*somax
  a0  = (somax2*somay - somaxy*somax)/float(den)
  a1  = (n*somaxy - somax*somay)/float(den)
 
  return a0,a1