


#########################################CREATING DATABASE######

import sqlite3
from soil import soil
import pandas as pd
import numpy as np
# Create your connection.

conn=sqlite3.connect('soilpro.db')
c=conn.cursor() 

##################CONVERT TO PANDA DATAFRAME##########
df = pd.read_sql_query("SELECT * FROM soil", conn) #conver database file to panda dataframe
c.execute('SELECT * FROM soil')
print(df)#PRINT TABLE

#####################COMPLETE##########


#######################################DATABASE COMPLETE########




######################################MODULE 1 CODE###############


print('''1.Sand (Nc, negative control)
2.Sub soil sandy (Ss)
3.Sandy loam (Sl)
4.Clay soil (Cl)
5.Sub soil loam (Sm)
6.Loam with compost (Lo)
7.Loam with leaf (Ll)
8.Compost (Pc, positive control)''')
a=int(input("Enter the no. of your soil type :"))


if a ==1 :
    f1=(input("Enter the dry matter in soil :"))
    if f1 in np.arange(df.iat[0,1],df.iat[0,2]) : #USING NUMPY RANGE FUNCTION
        b=1
    else :
        b=0
        
    f2=float(input("Enter the organic matter in soil :"))
    if f2 in np.arange(df.iat[0,3],df.iat[0,4]) :
        c=1
    else :
        c=0
    f3=float(input("Enter the pH value of soil :"))
    if f3 in np.arange(df.iat[0,5],df.iat[0,6]):
        d=1
    else :
        d=0
    f4=float(input("Enter the nitrogen % in soil :"))
    if f4 in np.arange(df.iat[0,7],df.iat[0,8]):
        e=1
    else :
        e=0
    f5=b+c+d+e
    if f5>= 3 :
        print("Soil is fertile")
    else :
        print("Infertile soil")

if a ==2 :
    f1=(input("Enter the dry matter in soil :"))
    if f1 in np.arange(df.iat[1,1],df.iat[1,2]) :
        b=1
    else :
        b=0
        
    f2=float(input("Enter the organic matter in soil :"))
    if f2 in np.arange(df.iat[1,3],df.iat[1,4]) :
        c=1
    else :
        c=0
    f3=float(input("Enter the pH value of soil :"))
    if f3 in np.arange(df.iat[1,5],df.iat[1,6]):
        d=1
    else :
        d=0
    f4=float(input("Enter the nitrogen % in soil :"))
    if f4 in np.arange(df.iat[1,7],df.iat[1,8]):
        e=1
    else :
        e=0
    f5=b+c+d+e
    if f5>= 3 :
        print("Soil is fertile")
    else :
        print("Infertile soil")

if a ==3 :
    f1=(input("Enter the dry matter in soil :"))
    if f1 in np.arange(df.iat[3,1],df.iat[3,2]) :
        b=1
    else :
        b=0
        
    f2=float(input("Enter the organic matter in soil :"))
    if f2 in np.arange(df.iat[3,3],df.iat[3,4]) :
        c=1
    else :
        c=0
    f3=float(input("Enter the pH value of soil :"))
    if f3 in np.arange(df.iat[3,5],df.iat[3,6]):
        d=1
    else :
        d=0
    f4=float(input("Enter the nitrogen % in soil :"))
    if f4 in np.arange(df.iat[3,7],df.iat[3,8]):
        e=1
    else :
        e=0
    f5=b+c+d+e
    if f5>= 3 :
        print("Soil is fertile")
    else :
        print("Infertile soil")

if a ==4 :
    f1=(input("Enter the dry matter in soil :"))
    if f1 in np.arange(df.iat[4,1],df.iat[4,2]) :
        b=1
    else :
        b=0
        
    f2=float(input("Enter the organic matter in soil :"))
    if f2 in np.arange(df.iat[4,3],df.iat[4,4]) :
        c=1
    else :
        c=0
    f3=float(input("Enter the pH value of soil :"))
    if f3 in np.arange(df.iat[4,5],df.iat[4,6]):
        d=1
    else :
        d=0
    f4=float(input("Enter the nitrogen % in soil :"))
    if f4 in np.arange(df.iat[4,7],df.iat[4,8]):
        e=1
    else :
        e=0
    f5=b+c+d+e
    if f5>= 3 :
        print("Soil is fertile")
    else :
        print("Infertile soil")

if a ==5 :
    f1=(input("Enter the dry matter in soil :"))
    if f1 in np.arange(df.iat[5,1],df.iat[5,2]) :
        b=1
    else :
        b=0
        
    f2=float(input("Enter the organic matter in soil :"))
    if f2 in np.arange(df.iat[5,3],df.iat[5,4]) :
        c=1
    else :
        c=0
    f3=float(input("Enter the pH value of soil :"))
    if f3 in np.arange(df.iat[5,5],df.iat[5,6]):
        d=1
    else :
        d=0
    f4=float(input("Enter the nitrogen % in soil :"))
    if f4 in np.arange(df.iat[5,7],df.iat[5,8]):
        e=1
    else :
        e=0
    f5=b+c+d+e
    if f5>= 3 :
        print("Soil is fertile")
    else :
        print("Infertile soil")

if a ==6 :
    f1=(input("Enter the dry matter in soil :"))
    if f1 in np.arange(df.iat[6,1],df.iat[6,2]) :
        b=1
    else :
        b=0
        
    f2=float(input("Enter the organic matter in soil :"))
    if f2 in np.arange(df.iat[6,3],df.iat[6,4]) :
        c=1
    else :
        c=0
    f3=float(input("Enter the pH value of soil :"))
    if f3 in np.arange(df.iat[6,5],df.iat[6,6]):
        d=1
    else :
        d=0
    f4=float(input("Enter the nitrogen % in soil :"))
    if f4 in np.arange(df.iat[6,7],df.iat[6,8]):
        e=1
    else :
        e=0
    f5=b+c+d+e
    if f5>= 3 :
        print("Soil is fertile")
    else :
        print("Infertile soil")

if a ==8 :
    f1=(input("Enter the dry matter in soil :"))
    if f1 in np.arange(df.iat[8,1],df.iat[8,2]) :
        b=1
    else :
        b=0
        
    f2=float(input("Enter the organic matter in soil :"))
    if f2 in np.arange(df.iat[8,3],df.iat[8,4]) :
        c=1
    else :
        c=0
    f3=float(input("Enter the pH value of soil :"))
    if f3 in np.arange(df.iat[8,5],df.iat[8,6]):
        d=1
    else :
        d=0
    f4=float(input("Enter the nitrogen % in soil :"))
    if f4 in np.arange(df.iat[8,7],df.iat[8,8]):
        e=1
    else :
        e=0
    f5=b+c+d+e
    if f5>= 3 :
        print("Soil is fertile")
    else :
        print("Infertile soil")
       
if a ==7 :
    f1=(input("Enter the dry matter in soil :"))
    if f1 in np.arange(df.iat[7,1],df.iat[7,2]) :
        b=1
    else :
        b=0
        
    f2=float(input("Enter the organic matter in soil :"))
    if f2 in np.arange(df.iat[7,3],df.iat[7,4]) :
        c=1
    else :
        c=0
    f3=float(input("Enter the pH value of soil :"))
    if f3 in np.arange(df.iat[7,5],df.iat[7,6]):
        d=1
    else :
        d=0
    f4=float(input("Enter the nitrogen % in soil :"))
    if f4 in np.arange(df.iat[7,7],df.iat[7,8]):
        e=1
    else :
        e=0
    f5=b+c+d+e
    if f5>= 3 :
        print("Soil is fertile")
    else :
        print("Infertile soil")

