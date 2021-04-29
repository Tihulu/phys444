#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.9

#libraries
import numpy as np
import math as m

#functions and constants
f = lambda x: m.exp((-(x-69)**2)/5.6) * (2.8 * m.sqrt(2*m.pi) )**(-1)
inc=0.393700787	#1 cm = 0.393700787 inches
	#boundaries
a=150*inc
b=182*inc
n=4
#main
def The_Simpsons(a,b,n,f):
	h=(b-a)/n
	odd=0
	even=0
	for i in range (1,n):
		if (i % 2) == 0:
			even=f(a+i*h) + even
		else:
			odd=f(a+i*h) + odd
	I= (h/3) * (f(a) + 4*odd + 2*even + f(b)) 
	return I
print (The_Simpsons(a,b,n,f))
f(1)