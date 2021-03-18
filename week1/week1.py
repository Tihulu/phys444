#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

import numpy as np
import math as m
import matplotlib.pyplot as plt
#funcs
def plot(t, y,exp_y):
	plt.title('y versus t')
	plt.xlabel('t')
	plt.ylabel('y')
	plt.plot(t, y , 'r.', label="Given Data")
	plt.plot(t, exp_y , 'b-', label="Fit")
	plt.grid(True)
	plt.legend()
	plt.savefig('week1_y_vs_t.png')
	plt.show()

#Numpy array [0,100]
t=np.arange(0,101)
#initials
v_0=5
g=10
y=[]
exp_y=[]
#formula
for i in range (len(t)):
	y.append( (v_0*t[i]) + (0.5*g*(t[i]**2)) )
#fit
#to obtain coeff.s I used this function. In here 2 stands for indicating that  the fit I want is 2^nd order polynomial
z = np.polyfit(t, y,2) 
for i in range (len(t)):
	exp_y.append(z[0]*(t[i]**2) + z[1]*t[i] + z[2] )
#values
print('t:',len(t),t)
print('y:',len(y),y)
print('coeffs:',len(z),z)
print('exp_y',len(exp_y),exp_y)
#plot
plot(t,y,exp_y)