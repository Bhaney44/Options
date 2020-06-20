#Derivative_Calculator

from math import *
from sympy import *

#------------------
#math

def f(x):
    return x ** 2

#For instance f(2) = 4

def derive(function, value):
    h = 0.00000000001
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    # Returns the slope to the third decimal
    return float("%.3f" % slope)

x = derive(f, 2)


def g(x):
    return(sin(x) * cos(x) + exp(2*x) + 2*x**4 - 10)

#print(g(x))
#print(g(-1))
#print(derive(g, -1))

#------------------
#SymPy

#Calculus

x, y, z = symbols ('x y z')
#init_printing(use_unicode=True)

print('derivative of x =', (diff(cos(x), x))
print('derivative of x^2 ='diff(exp(x**2),x))
