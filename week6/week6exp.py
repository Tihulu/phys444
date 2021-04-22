import numpy as np
import math as m
f = lambda x: m.pow(x,m.cos(x))
def fp(x): return m.pow(x,(-1 + m.cos(x))) * (m.cos(x) - x*m.log(x)*m.sin(x))
print(fp(0.6))

def phi(x,h): return (f(x+h)-f(x-h))/(2*h)
d = [phi(0.6,h) for h in [2**(-n) for n in range(5)]]
print(d)
N = len(d)
print(N)
D = np.zeros((N,N))
D[:,0] = d
for m in range(1,N):
    for n in range(m,N):
        D[n,m] = (4**m*D[n,m-1]-D[n-1,m-1])/(4**m-1)
        print(n,m)


print(D)

