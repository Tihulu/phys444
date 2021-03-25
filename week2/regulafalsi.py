import numpy as np
import math as m

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
		if abs(f(xr))<t:
			print('xr',xr)
			break
		if f(xr)<0:
			xl=xr
			fl=f(xr)
			print('xl',xl)
		if f(xr)>0:
			xu=xr
			fu=f(xr)
			print('xu',xu)			
	return xr

def p_error(app_val,exact_val):
	err=(abs(app_val - exact_val)/abs(exact_val))
	perct_err=err*100
	return perct_err

f = lambda x: x**2 - 3
t=0.000001

r1=regulafalsi(f,-2,-1,t)
print('regulafalsi, root1:',r1,'with tolerance:',t,'and with', p_error(r1,-m.sqrt(3)),'percent error')
r2=regulafalsi(f, 1, 2,t)
print('regulafalsi, root2:',r2,'with tolerance:',t,'and with', p_error(r2,m.sqrt(3)),'percent error')
