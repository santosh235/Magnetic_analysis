"""
Created on Wed Oct 28 15:14:33 2020

@author: santosh
"""

import numpy as np


def coercivity_cal(tot_data):

    #Right Half of quadrant
    right_half = (tot_data[:,1][tot_data[:,0]>0])
    
    moment_1st = np.min(right_half[right_half > 0])
    field_1st = tot_data[:,0][tot_data[:,1] == moment_1st][0]
    
    moment_4th = np.max(right_half[right_half < 0])
    field_4th = tot_data[:,0][tot_data[:,1] == moment_4th][0]
    
    m_coercivity_right , c_right = np.polyfit([field_1st, field_4th], [moment_1st, moment_4th], 1)
    
    x_coercivity_right = -(c_right / m_coercivity_right)
    
    #Left Half of quadrant
    left_half = (tot_data[:,1][tot_data[:,0]<0])
    
    moment_2nd = np.min(left_half[left_half > 0])
    field_2nd = tot_data[:,0][tot_data[:,1] == moment_2nd][0]
    
    moment_3rd = np.max(left_half[left_half < 0])
    field_3rd = tot_data[:,0][tot_data[:,1] == moment_3rd][0]
    
    m_coercivity_left , c_left = np.polyfit([field_2nd, field_3rd], [moment_2nd, moment_3rd], 1)
    
    x_coercivity_left = -(c_left / m_coercivity_left)
    
    
    
    coercivity = [x_coercivity_right, x_coercivity_left]
    
    return coercivity



def remanence_cal(tot_data):
    top_half = (tot_data[:,0][tot_data[:,1]>0])

    rem_field_1st = np.min(top_half[top_half > 0])
    rem_moment_1st = tot_data[:,1][tot_data[:,0] == rem_field_1st][0]
    
    rem_field_2nd = np.max(top_half[top_half < 0])
    rem_moment_2nd = tot_data[:,1][tot_data[:,0] == rem_field_2nd][0]
    
    m_rem_top, c_top = np.polyfit([rem_field_1st, rem_field_2nd], [rem_moment_1st, rem_moment_2nd], 1)
    
    
    
    #Bottom Half
    bottom_half = (tot_data[:,0][tot_data[:,1]<0])
    
    rem_field_4th = np.min(bottom_half[bottom_half > 0])
    rem_moment_4th = tot_data[:,1][tot_data[:,0] == rem_field_4th][0]
    
    rem_field_3rd = np.max(bottom_half[bottom_half < 0])
    rem_moment_3rd = tot_data[:,1][tot_data[:,0] == rem_field_3rd][0]
    
    m_rem_bottom, c_bottom = np.polyfit([rem_field_3rd, rem_field_4th], [rem_moment_3rd, rem_moment_4th], 1)
    
    remanence = [c_top, c_bottom]
    
    return remanence