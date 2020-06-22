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


#print(df.columns)
#print(df.columns[0])
#print(df.columns[1])
#print(df.columns[2])

claims = df.columns[0]
prior_art = df.columns[1]
inventors = df.columns[2]

#for index, row in df.iterrows():
    #print(claims, prior_art, inventors)

    

#with open('Total_Python.csv','r') as csvfile:
   # plots = csv.reader(csvfile, delimiter=',')
   # for row in plots:
       # x.append(int(row[0]))
       # y.append(int(row[1]))
       # z.append(int(row[2]))


#threedee = plt.figure().gca(projection='3d')
#threedee.scatter(claims, prior_art, inventors)
#threedee.set_xlabel('Claims')
#threedee.set_ylabel('Cited Proior Art')
#threedee.set_zlabel('Inventors')


#plt.title('Thyroid Patents')
#plt.legend()
#plt.show()
