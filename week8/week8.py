#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.1

#libraries
import numpy as np
import math as m
import matplotlib.pyplot as plt
#functions and constants
f = lambda x: m.exp(x) * m.cos(x)
a=0.5
b=1.5
def plot(f,a,b,n,x1,x2,x3,name,title,xlabel,ylabel,labelname,labelname1,pointer,pointer2):
	#first plot
	y=[f(x1),f(x2),f(x3) ]
	x=[x1,x2,x3]
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(x, y , pointer, label=labelname)
	#second plot
	y_1=[f(a)]
	x_1=[a]
	h=(b-a)/n #for n steps
	for i in range (1,n):
		y_1.append(f(a+i*h))
		x_1.append(a+i*h)
	y_1.append(f(b))
	x_1.append(b)
	plt.plot(x_1, y_1 ,pointer2 , label=labelname1)
	plt.grid(True)
	plt.legend()
	plt.savefig(name+'.png')
	plt.show()
def Gauss_Quad(f,a,b):
	x3=((b-a)/2)*0.7745966692 + ((b+a)/2) #Three point Gauss quadrate x axis number for normal distr.
	x1=((b-a)/2)*(-0.7745966692) + ((b+a)/2) #Three point Gauss quadrate x axis number for normal distr.
	x2=0+ ((b+a)/2) #Three point Gauss quadrate x axis number for normal distr.
	c=((b-a)/2) # If we take sum of all c values the result will be 2 which means we count the interval twice 
	c1=c3=0.5555555556 #Three point Gauss quadrate multiplying const.s
	c2=0.8888888889 #Three point Gauss quadrate multiplying const.s

	I=c*( c1*f(x1) + c2*f(x2) + c3*f(x3) ) #integration (aproximately)
	print(I)
	plot(f,a,b,100,x1,x2,x3,'Plot','Gauss Quadrate','X','Y','integrated func.','function','r-','b-')
	return I
#main
Gauss_Quad(f,a,b)