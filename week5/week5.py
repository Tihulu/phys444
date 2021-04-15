#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

#libraries
import numpy as np
import math as m

#constants
rho = 1800
k = 3.5*10**(-7)
C = 840

#data
z = [0,1.25,2.5]
Tarr = [10, 12, 13.5]

#main

#FD
h = abs(z[0] - z[1])
def T(x,arr1,arr2):
	return arr1[z.index(x)]
FD = lambda x: (T(x+h,Tarr,z) - T(x,Tarr,z) )/h
print ('FD dT/dz:',FD(0))
#MFD
MFD = lambda x: (-T(x+(2*h),Tarr,z) + 4*T(x+h,Tarr,z) - 3*T(x,Tarr,z) ) / (2*h)
print ('MFD dT/dz:',MFD(0))
#Formulation
qFD = lambda z: -k*rho*C*FD(z)
qMFD = lambda z: -k*rho*C*MFD(z)
print ('q with FD:',qFD(0),'heat is transferred from the soil to the air')
print ('q with MFD:',qMFD(0),'heat is transferred from the soil to the air')