from math import*

def f(x):
    return x**2

def derive(function, value):
    h = 0.0001
    top = function(value + h) - function(value)
    bottom = h
    slope = top/bottom

    #Returns the slope of the third decimal
    return float("%.3f" %slope)

print(derive(f,2))
