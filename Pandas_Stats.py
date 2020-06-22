import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('Lite_Coin_12_Mos.csv')


print(df.head())

print(df.tail())
print(df.index)
print(df.columns)
print("-----")

print(df.describe())

#print mediuan
print('median')
print(df.median())
print("-----")

#Mode
print('mode')
print(df.mode())
print("-----")
#Variance
##In probability theory and statistics, variance is the expectation of the squared deviation of a random variable from its mean.
##Informally, it measures how far a set of numbers are spread out from their average value.
print('variance')
print(df.var())
print("-----")
#Co-Variance
##In probability theory and statistics, covariance is a measure of the joint variability of two random variables.
##If the greater values of one variable mainly correspond with the greater values of the other variable,
##and the same holds for the lesser values, the covariance is positive.
print('co-variance')
print(df.cov())

#Cumsum
#print('Cumsum')
#print(df.cumsum())

#Scalar Map
#print('Map')
#print(df.applymap())

#Multiply
#print('Multiply')
#print(df.mul())

#Modulo
#print('Modulo')
#print(df.mod())





