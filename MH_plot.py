"""
Created on Mon Oct 26 17:55:59 2020

@author: santosh
"""

# PLotting Graph
import matplotlib.pyplot as plt
import numpy as np


def all_plot(x, y, y_corr, x_dia, m_dia, c_dia, T, out_file):
    
    #Plot Setup
    plt.xlim(np.min(x),np.max(x))
    plt.ylim(min(np.min(y) ,np.min(y_corr)) ,(max(np.max(y) ,np.max(y_corr))))
    plt.xlabel("Mag Field (Oe)")
    plt.ylabel("Moment (emu)")
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    plt.title("M-H analysis at T = " + str(T) + 'K')
    plt.axvline(x=0, color='k', linestyle='--', alpha=0.6)
    plt.axhline(y = 0, color='k', linestyle='--', alpha=0.6)
    
    #Data Plotting
    plt.plot(x, y, color = 'r', label ='Raw data')
    plt.plot(x, y_corr, color = 'b', label = 'Corrected')
    plt.plot(x, (m_dia * x), color = 'c', label = 'Dia Contribution ')
    plt.plot(x_dia, (m_dia * x_dia + c_dia), linewidth=6, alpha = 0.5, label = 'dia fit', color='yellow')
    plt.legend()
    
    #Saving Figure
    plt.savefig((out_file + "_all_plot.png"), bbox_inches='tight', dpi=300)
    plt.close()


def corr_plot(x, y_corr, c_sat, T, field_sat, coercivity, remanence):
    
    #Plot Setup
    plt.xlim(np.min(x),np.max(x))
    plt.xlabel("Mag Field (Oe)")
    plt.ylabel("Moment (emu)")
    plt.title("Corrected M-H plot")
    plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    plt.axvline(x=0, color='k', linestyle='--', alpha=0.6)
    plt.axhline(y = 0, color='k', linestyle='--', alpha=0.6)
    plt.legend(['T = '  + str(T) + 'K'])
    
    #Data Plotting
    plt.plot(x,y_corr,color = 'b', linestyle='-', marker='o', linewidth=1, markersize = 3)
    plt.plot(x[x > 0], (x [x > 0] * 0 + c_sat), linestyle='--')
    plt.plot(0,c_sat, marker = '*', markersize = 12)
    plt.plot((field_sat, field_sat), (0, c_sat), '--')
    plt.plot(coercivity, [0,0], marker = '*',markersize = 14)
    
    
  #  plt.plot(x_coercivity_left, 0, marker = '*', markersize = 12)
    plt.plot([0,0], remanence, marker = '*',markersize = 14)
   # plt.plot(0,c_bottom, marker = '*', markersize = 16, color='r')
    #Displaying Figure.
    plt.show()
