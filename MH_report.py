"""
Created on Mon Oct 26 18:09:09 2020

@author: santosh
"""
from datetime import date
import numpy as np
import csv

def corr_data(x, y, y_corr, out_file):
    data = np.array([x, y, y_corr])
    data = data.T
    
    file = out_file + "_corrected_file.csv"
    with open(file, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Mag Field','Moment','Corrected Moment'])
        np.savetxt(f, data, delimiter=',')


def report(data_file, out_file, m_dia, field_sat, c_sat, coercivity, remanence):
    today = date.today()
    today = today.strftime("%B %d, %Y")
    report_file = out_file + "_report.txt"
    report = open(report_file, "w")
    report.write("Report Generation on : " + today + '\n')
    report.write("This is an auto-generated report for the analysis of the file : " + data_file + '\n\n')
    report.write("Diamagnetic slope :" + str(m_dia) + '\n')
    report.write("Saturation Field : " + str(field_sat) + '\n')
    report.write("Saturation Moment : " + str(c_sat) + '\n')
    report.write("Coercivity : " + str(coercivity) + '\n')
    report.write("Remanence : " + str(remanence) + '\n')
    report.close()
