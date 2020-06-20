#Matrix Math
import numpy as np

#matrix arrays
x = np.array([1,5,2])
y = np.array([7,4,1])

#addition
x + y
array([8, 9, 3])

#multiplication
x * y
array([ 7, 20,  2])

#substraction
x - y
array([-6,  1,  1])
#division
x / y
array([0, 1, 2])

#Modulus - absolute value or a constant ratio
x % y
array([1, 1, 0])

#Vector Addition and Subtraction
x = np.array([3,2])
y = np.array([5,1])
z = x + y
z
array([8, 3])

#Scalar Product and Dot Product
x = np.array([1,2,3])
y = np.array([-7,8,9])
np.dot(x,y)
36

dot = np.dot(x,y)
x_modulus = np.sqrt((x*x).sum())
y_modulus = np.sqrt((y*y).sum())

# cosine of angle between x and y
cos_angle = dot / x_modulus / y_modulus 
angle = np.arccos(cos_angle)
angle
0.80823378901082499

# angle in degrees
angle * 360 / 2 / np.pi 
46.308384970187326

#Matrix class
x = np.array( ((2,3), (3, 5)) )
y = np.array( ((1,2), (5, -1)) )
x * y
array([[ 2,  6],
       [15, -5]])
x = np.matrix( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)) )
x * y
matrix([[17,  1],
        [28,  1]])

#Matrix product
x = np.array( ((2,3), (3, 5)) )
>>> y = np.matrix( ((1,2), (5, -1)) )
>>> np.dot(x,y)
matrix([[17,  1],
        [28,  1]])

np.mat(x) * np.mat(y)
matrix([[17,  1],
        [28,  1]])

#Practical Application
NumPersons = np.array([[100,175,210],[90,160,150],[200,50,100],[120,0,310]])
Price_per_100_g = np.array([2.98,3.90,1.99])
Price_in_Cent = np.dot(NumPersons,Price_per_100_g)
Price_in_Euro = Price_in_Cent / np.array([100,100,100,100])
Price_in_Euro
array([ 13.984, 11.907, 9.9, 9.745])

#Cross Product
x = np.array([0,0,1])
y = np.array([0,1,0])

np.cross(x,y)
array([-1,  0,  0])

np.cross(y,x)
array([1, 0, 0])



