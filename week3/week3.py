#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

#libraries
import numpy as np
import math as m
import matplotlib.pyplot as plt

#functions
def Newton(f,df,x, t):
	i=0
	while True:
		dx= -f(x)/df(x)
		x = x + dx
		if abs(dx) < t:
			er=dx
			return x, i ,er
			break
		i=i+1

def plot(x1, y1,name,title):
	plt.title(title)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.plot(x1, y1 , 'r-', label="function")
	plt.grid(True)
	plt.legend()
	plt.savefig(name)
	plt.show()

#inputs
f = lambda x: x**4-6.4*x**3  + 6.45*x**2 + 20.538*x -31.752
df = lambda x: 4.0*x**3 -19.2*x**2 + 12.9*x + 20.538
#here lambda function is a short cut to represent our equation as a function of f
t=10**(-6) #tolerance level

#main
root1,numIter1,err1 = Newton(f,df,2.0,t)
root2,numIter2,err2 = Newton(f,df,-2.0,t)
root3,numIter3,err3 = Newton(f,df,4.0,t)
print ('root1 =',root1,'\n number of iteration =',numIter1,'\n error =',err1)
print ('\nroot2 =',root2,'\n number of iteration =',numIter2,'\n error =',err2)
print ('\nroot3 =',root3,'\n number of iteration =',numIter3,'\n error =',err3)

#plot
bin=10**6
q=np.linspace(-5,5, bin, endpoint=True)
f_arr=[]
df_arr=[]
for i in range (len(q)):
	f_arr.append(f(q[i]))
	df_arr.append(df(q[i]))
title=str('f(x) vs x')
name=str('fvsx.png')
plot(q,f_arr,name,title)
title2=str('df(x)/dx vs x')
name2=str('dfvsx.png')
plot(q,df_arr,name2,title2)