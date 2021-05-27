import numpy as np
import math as m
import matplotlib.pyplot as plt
def plot(x1, y1,name,title):
	plt.title(title)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.plot(x1, y1 , 'r-', label="function")
	plt.grid(True)
	plt.legend()
	plt.savefig(name)
	plt.show()
# Limits: 0.0 <= t <= 2.0
a=0.0
b=2.0
#steps
N=10
#step size4
h= (b-a)/N
#initial val: y(0.0) = 0.5
IV = (0.0,0.5)
#ODE
def f(t,y):
	return y - t**2 +1
#arrays to hold t and y
t = np.arange( a, b+h, h )
w = np.zeros((N+1,))
#IC's
t[0], w[0] = IV
#Eulers meth.
for i in range(1,N+1):
	w[i] = w[i-1] + h * f( t[i-1], w[i-1] )
# exact solution
def y( t ):
	return (t+1.0)**2.0-0.5*np.exp(t)
plot(t,w,'euler_example.png', 'apprx')
plot(t, y(t),'euler_exact.png', 'exact' )