#Matrix Algebra

import numpy as np


#Define all matrices

A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1;6 0')
D = np.matrix('3 -2 -1; 1 2 3')

u = np.matrix('6 2 -3 5')
v = np.matrix('3 5 -1 4')
w = np.matrix('1; 8; 0; 5')


print "1.1) Dim A = ", A.shape
print "1.2) Dim B = ", B.shape
print "1.3) Dim C = ", C.shape
print "1.4) Dim D = ", D.shape
print "1.5) Dim u = ", u.shape
print "1.6) Dim v = ", v.shape, '\n'

a = 6

print "2.1) u+v = ", u+v
print "2.2) u-v = ", u-v
print "2.3) a*u = ", a*u
print "2.4) u dot v = ", np.vdot(u, v)
print "2.5) ||u|| = ", np.linalg.norm(u), '\n'

print "3.1) A+C = not defined"
print "3.2) A-C.T = \n" , (A-C.T)
print "3.3) (C.T + 3*D) = \n", (C.T + 3*D)
print "3.4) B*A = \n", np.dot(B, A)
print "3.5) B*A.T = not defined"
print "3.6) B*C = not defined"
print "3.7) C*B = \n", C*B
print "3.8) B^4 = \n", np.linalg.matrix_power(B, 4)
print "3.9) A*A.T = \n", A*A.T
print "3.10) D.T*D = \n", D.T*D

"""
Results:

1.1) Dim A =  (2, 3)
1.2) Dim B =  (2, 2)
1.3) Dim C =  (3, 2)
1.4) Dim D =  (2, 3)
1.5) Dim u =  (1, 4)
1.6) Dim v =  (1, 4) 

2.1) u+v =  [[ 9  7 -4  9]]
2.2) u-v =  [[ 3 -3 -2  1]]
2.3) a*u =  [[ 36  12 -18  30]]
2.4) u dot v =  [[51]]
2.5) ||u|| =  8.60232526704 

3.1) A+C = not defined
3.2) A-C.T = 
[[-4 -7 -3]
 [ 3  6  4]]
3.3) (C.T + 3*D) = 
[[14  3  3]
 [ 2  7  9]]
3.4) B*A = 
[[-1 -5 -1]
 [ 2  7  4]]
3.5) B*A.T = not defined
3.6) B*C = not defined
3.7) C*B = 
[[ 5 -6]
 [ 9 -8]
 [ 6 -6]]
3.8) B^4 = 
[[ 1 -4]
 [ 0  1]]
3.9) A*A.T = 
[[14 28]
 [28 69]]
3.10) D.T*D = 
[[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]
 """
