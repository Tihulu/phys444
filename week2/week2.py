#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

#libraries
import numpy as np
import math as m
import matplotlib.pyplot as plt

#functions
def plot(x1, y1):
	plt.title('f versus x')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.plot(x1, y1 , 'r-', label="function")
	plt.grid(True)
	plt.legend()
	plt.savefig('f vs x')
	plt.show()

def bisection(f,a,b,t):
	while (b-a)>t :
		m= (b+a)/2.0
		y_m=f(m)
		y_a=f(a)
		if (y_m > 0 and y_a < 0) or (y_m < 0 and y_a > 0): #to check are they in opposite sign
			b=m
			#print('b',m)
		else:
			a=m
			#print('a',m)
	return m
def regulafalsi(f,a,b,t):
	if f(a)<0 and f(b)>0:
		fl=f(a)
		xl=a
		fu=f(b)
		xu=b
	if f(a)>0 and f(b)<0:
		fl=f(b)
		xl=b
		fu=f(a)
		xu=a
	while 1:
		xr= (xl*fu-xu*fl)/(fu-fl)
		if abs(f(xr))<t: # here t can be acceptable as 0
			#print('xr',xr)
			break
		if f(xr)<t:
			xl=xr
			fl=f(xr)
			#print('xl',xl)
		if f(xr)>t:
			xu=xr
			fu=f(xr)
			#print('xu',xu)			
	return xr
def p_error(app_val,exact_val): #error function
	err=(abs(app_val - exact_val)/abs(exact_val))
	perct_err=err*100
	return perct_err

	

f = lambda x: x**2 - 3 #the function that we are searching its roots. 
#here lambda function is a short cut to represent our equation as a function of f
t=0.000001 #tolerance level

#calculation
r1=bisection(f,-2,-1, t)
print('bisection, root1:',r1,'with tolerance:',t,'and with', p_error(r1,-m.sqrt(3)),'percent error')
r2=bisection(f, 1, 2, t)
print('bisection, root2:',r2,'with tolerance:',t,'and with', p_error(r2,m.sqrt(3)),'percent error')

r1=regulafalsi(f,-2,-1,t)
print('regulafalsi, root1:',r1,'with tolerance:',t,'and with', p_error(r1,-m.sqrt(3)),'percent error')
r2=regulafalsi(f, 1, 2,t)
print('regulafalsi, root2:',r2,'with tolerance:',t,'and with', p_error(r2,m.sqrt(3)),'percent error')

#plot
bin=1000
q=np.linspace(-10,10, bin, endpoint=True)
f_arr=[]
for i in range (len(q)):
	f_arr.append(f(q[i]))
plot(q,f_arr)