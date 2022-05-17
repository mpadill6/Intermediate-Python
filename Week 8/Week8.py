# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:22:43 2020

@author: mpadilla
"""
#Part I
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("all_alpha_19.csv", header="infer")
T3B125_Gasoline_Diesel=df.query("Stnd == 'T3B125' & ( Fuel=='Gasoline' | Fuel=='Diesel') ")
print(T3B125_Gasoline_Diesel)
Filtered=T3B125_Gasoline_Diesel.filter(['Model', 'Displ', 'Fuel','City MPG', 'Hwy MPG', 'Cmb MPG', 'Greenhouse Gas Score']).reset_index(drop=True)
Filtered=Filtered.astype({'City MPG': float,'Hwy MPG': float,'Cmb MPG': float})
print(Filtered['City MPG'].dtype)
print(Filtered['Hwy MPG'].dtype)
print(Filtered['Cmb MPG'].dtype)
def mpg_to_kml(mpg):
    return mpg*0.42514
Filtered=Filtered.assign(City_KML = mpg_to_kml(Filtered['City MPG']))
Filtered=Filtered.assign(Hwy_KML = mpg_to_kml(Filtered['Hwy MPG']))
Filtered=Filtered.assign(Cmb_KML = mpg_to_kml(Filtered['Cmb MPG']))

Filtered.to_csv("car_data.csv", header=True, index=True, index_label='Index ID')



#%%
#Part II
df=pd.read_csv('car_data.csv', header="infer", index_col=0)
x=df['Displ']
y=df['City MPG']
plt.scatter(x,y,color='r' )
plt.xlabel("Displ")
plt.ylabel("City MPG")
plt.show()

def size_score(score):
    return score*10

Fuel_string=df["Fuel"].tolist()

df=df.assign(s=size_score(df['Greenhouse Gas Score']))

color_list=[]
for i in range (0,len(Fuel_string)):
    if Fuel_string[i]=='Gasoline':
        color_list.append('r')
    if Fuel_string[i]=='Diesel':
        color_list.append('g')

df['Color_code']=color_list
gas=df.query("Fuel=='Gasoline'")
diesel=df.query("Fuel=='Diesel'")
x_gas=gas['Displ']
y_gas=gas['City MPG']

x_diesel=diesel['Displ']
y_diesel=diesel['City MPG']

plt.scatter(x_gas,y_gas,color=gas['Color_code'],s=gas['s'],alpha=0.5, label='Gasoline')
plt.scatter(x_diesel,y_diesel,color=diesel['Color_code'],s=diesel['s'],alpha=0.5, label='Diesel')
plt.xlabel("Engine Displacement (size of Engine)")
plt.ylabel("City Miles per Gallon")
plt.title("Fuel Efficiency as a Function of Engine Size")
plt.legend()
plt.show()

#%%
#Extra Plot
#City MPG
x_efficiency_city=df['City MPG']
plt.hist(x_efficiency_city,bins=70)
plt.xlabel("City MPG")
plt.ylabel('Counts')
plt.title('City Fuel Efficiency Histogram')
plt.show()


x_efficiency_hwy=df['Hwy MPG']
plt.hist(x_efficiency_hwy,bins=70)
plt.xlabel("Hwy MPG")
plt.ylabel('Counts')
plt.title('Hwy Fuel Efficiency Histogram')
plt.show()

x_efficiency_cmb=df['Cmb MPG']
plt.hist(x_efficiency_cmb,bins=70)
plt.xlabel("Cmb MPG")
plt.ylabel('Counts')
plt.title('Combined Fuel Efficiency Histogram')
plt.show()