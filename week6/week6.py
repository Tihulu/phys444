#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.1

#libraries
import numpy as np
import math as m

#functions and constants
f = lambda x: m.pow(x,m.cos(x))
x=0.6 #at x=0.6
h=0.1 #R. extrp.
CD= lambda h: (f(x+h)-f(x-h))/(2*h) #Central Diff
phi= lambda n: CD(h/(2**n)) 
#main
def D(n,m): #This is a recursive function. Instead of coding complex loops this method is much more clear if have initial function value such as D(n,0)
	if m==0:
		Der = phi(n)
		#print (Der,'n=',n,'m=',m)
		return Der
	else:
		Der= D(n,m-1) + ( (D(n,m-1) - D(n-1,m-1)) * (1/((4**m)-1)))
		#print (Der,'n=',n,'m=',m)
		return Der

print('\n Derivative of the function f(x)=x^cos(x) at x=',x,', h=',h,', n=',5,', m=',5, '\n', " f'(0.6) = ", D(5,5))
