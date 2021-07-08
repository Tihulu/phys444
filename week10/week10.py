#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.1

import numpy as np
import math as m
import matplotlib.pyplot as plt
#funcs
	#ODE
def f(x,u):
	return x**2 * m.exp(-(u+1))

# Limits: 0.0 <= x <= 3.0
a=0.0
b=3.0
# IV's
IV = (0.0,1.0) #x ,u
alpha=1
#steps
N=300
#step size
h= (b-a)/N #h=0.01
#arrays to hold t and y
x = [0]
u = [0]
for i in range(1,N+1):
	x.append( h*i ) #x_i = 0.01*i
#IC's
x[0], u[0]= IV
#RK2
for i in range(N):
	K1= h*f( x[i], u[i] )
	K2= h*f(x[i]+h*alpha , u[i]+K1*alpha)
	u.append( u[i] + K1*(1-(1/(2*alpha))) + K2*(1/(2*alpha)) )


# plot

plt.title('Runge - Kutta 2')
plt.xlabel('x')
plt.ylabel('u')
plt.plot(x, u , 'r-')
plt.grid(True)
plt.legend()
plt.savefig('rgk2.png')
plt.show()
