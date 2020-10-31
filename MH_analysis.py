"""
Created on Sun Oct 25 16:16:41 2020

@author: santosh
"""

# MH Analysis of SQUID data file

import numpy as np
import csv
from MH_plot import *
from MH_report import *
from MH_plotly import *
from MH_coercivity_remanence import *

# data_file = input("Enter file name:")
# data_file = "../" + data_file

#out_file = input("Enter output file name: ")
#out_file = "../" + out_file
#T = input("Enter the temp: ")

data_file = "../6K.dat"
out_file = '../s'
T = 10

# head = int(input("Enter the number of starting line to omit: "))
# dia = int(input("Enter the points in diamagnetic region: "))
head = 26
dia =10

#Read from CSV file
x = np.array([])
y = np.array([])
with open(data_file, 'r') as file:
    line = csv.reader(file)
    for skip in range(head):
        next(line)  
    for row in line:
    	x = np.append(x, [float(row[3])])
    	y = np.append(y, [float(row[37])])

# Extracting Diamagnetic data
x_dia = np.array([])
y_dia = np.array([])
for i in range(-1,-dia,-1):
    x_dia = np.append(x_dia, [x[i]])
    y_dia = np.append(y_dia, [y[i]])





# Fitting straight line to Diamagnetic region 
m_dia, c_dia = np.polyfit(x_dia, y_dia, 1)

#Diamagnetic Correction
y_corr = y - (m_dia * x)
tot_data = np.array([x, y_corr]).T


#Saturation Calculation by fitting straight line to corrected data
c_sat = np.average(y_corr[-dia:-1])
field_sat = np.min(tot_data[:,0][tot_data[:,1]>c_sat])

#Coercivity Calculation
coercivity = coercivity_cal(tot_data)



# Remanence Calculation
remanence = remanence_cal(tot_data)


# #Plot of Original, Corrected and diamagnetic data
#all_plot(x, y, y_corr, x_dia, m_dia, c_dia, T, out_file)


#Plot of Corrected Data
corr_plot(x, y_corr, c_sat, T, field_sat, coercivity, remanence)


# #Data File for corrected data
#corr_data(x, y, y_corr, out_file)


# #Report file
report(data_file, out_file, m_dia, field_sat, c_sat, coercivity, remanence )

