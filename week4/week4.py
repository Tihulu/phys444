#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

#libraries
import numpy as np
import math as m

#Arrays
A=[[1,-1,2,1],[3,2,1,4],[5,-8,6,3],[4,2,5,3]]
x1,x2,x3,x4=0,0,0,0
X=[x1,x2,x3,x4]
B=[1,1,1,-1]
#print(A[0][1])
S=np.amax(np.absolute(A),1) #finds max values on each row
#print(S)
#print(len(A))
L=np.arange(len(A))


Q=L
R=[0,0,0,0]
#main
for j in range(len(L)-1):
	absA=np.absolute(A)
	for i in (L):
		R[i]=((absA[L[i]][j])/S[L[i]]) #to find max corresponding index on L
	for i in range(j):
		R[i]=-1
	iR=np.argmax(R)
	#print(j,R)
	mem=L[iR]
	L[iR]=L[j]
	L[j]=mem
	Q=np.delete(Q,np.where(Q == L[j])) #delete element which is L[j]
	#print(j,Q)
	#print(j,L)
	QR=L[j]
	#print(j,QR,A[QR])
	for i in (Q):
		elc=(A[i][j])/(A[QR][j]) #elemination constant for row elemination
		A[i]=A[i]-np.multiply(elc,A[QR]) #scalar multiplication
		B[i]=B[i]-(elc*B[QR])
#print(A)
#print(B)
le=len(L)-1
for i in (L):
	m=0
	for y in range(len(L)):
		m=(A[L[i]][le-y])*(X[le-y]) + m
	X[i]=(B[L[i]]-m)/(A[L[i]][i])
print('Solution Set:',X)
#Residiues
A=[[1,-1,2,1],[3,2,1,4],[5,-8,6,3],[4,2,5,3]]
B=[1,1,1,-1]
R=np.dot(A,X) - B
print('Residiue Set:',R)