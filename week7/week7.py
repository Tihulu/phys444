#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.9

#libraries
import numpy as np
import math as m
import matplotlib.pyplot as plt

#functions and constants
f = lambda x: m.exp((-(x-69)**2)/5.6) * (2.8 * m.sqrt(2*m.pi) )**(-1)
inc=0.393700787	#1 cm = 0.393700787 inches
	#boundaries
abraham=150*inc
bart=182*inc
n=1000 # # of segments
#main
	#functions
def The_Simpsons(a,b,n,f):
	homer=(b-a)/n
	odd=0
	even=0
	for i in range (1,n):
		if (i % 2) == 0:
			even=f(a+i*homer) + even
		else:
			odd=f(a+i*homer) + odd
	I= (homer/3) * (f(a) + 4*odd + 2*even + f(b)) 
	return I

def plot(f,a,b,n,name,title,xlabel,ylabel,labelname):
	y=[f(a)]
	x=[a]
	h=(b-a)/n
	for i in range (1,n):
		y.append(f(a+i*h))
		x.append(a+i*h)
	y.append(f(b))
	x.append(b)
	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(x, y , 'r-', label=labelname)
	plt.grid(True)
	plt.legend()
	plt.savefig(name+'.png')
	plt.show()

	#print plot

print ('The probability of an Turkish male is between 150 cm and 182 cm is: %',100*The_Simpsons(abraham,bart,n,f))
plot(f,60,80,n,'Turkish_male_height','Turkish male height distribution','height in inches','prob density','f(x)')
