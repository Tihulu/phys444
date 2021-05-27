#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

import numpy as np
import math as m
import matplotlib.pyplot as plt
#funcs
	#ODE
def f(t,v):
	return 1 - 2*(v**2) - t
	
	#analytically v''(t) = -4*v*v'-1
def f2nd(t,v):
	return -4*v*(f(t,v))-1
	#analytically v'''(t) = -4*v'-4*v*v''
def f3rd(t,v):
	return -4*(f(t,v)) -4*v*(f2nd(t,v))
# Limits: 0.0 <= t <= 1.0
a=0.0
b=1.0
# IV's
IV = (0.0,1.0)
#steps
N=100
#step size
h= (b-a)/N #h=0.01
#arrays to hold t and y
t = [0]
w = [0]
ww = [1.0]
www =[1.0]
#IC's
t[0], w[0]= IV

#Eulers meth.
for i in range(1,N+1):
	t.append( h*i ) #t_i = 0.01*i

for i in range(1,N+1): #with first order derivative
	w.append(w[i-1] + h * f( t[i-1], w[i-1] ))

for i in range(1,N+1): #with second order derivative
	ww.append( w[i] + (h**2)*0.5*f2nd( t[i-1], w[i-1] ) ) 

for i in range(1,N+1): #with third order derivative
	www.append( ww[i] + ((h**3)/6) *f3rd( t[i-1], w[i-1] ) ) 
# plot

plt.title('Euler apprx')
plt.xlabel('t')
plt.ylabel('v')
plt.plot(t, w , 'r-', label="apprx with 1st order")
plt.plot(t, ww , 'b-', label="apprx with 2nd order")
plt.plot(t, www , 'g-', label="apprx with 3rd order")
plt.grid(True)
plt.legend()
plt.savefig('euler.png')
plt.show()
