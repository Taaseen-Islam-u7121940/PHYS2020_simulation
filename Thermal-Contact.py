# -*- coding: utf-8 -*-
"""
Module: Thermal-Contact
Contains code for modelling thermal contact
"""

import numpy as np
from numpy import random as rng
import pandas as pd
import matplotlib.pyplot as plt

def step_time(contact_list):
    #NOTE: edits global variable
    return_list = contact_list
    index = 0
    while index < len(contact_list) - 1:
        if contact_list[index] != contact_list[index+1]:
            swap = rng.random(1)
            if swap>0.5:
                return_list[index]   = 1 - return_list[index]
                return_list[index+1] = 1 - return_list[index+1]
            index += 2
        else:
            index += 1
    return return_list



def exchange(n=10, m=8, max_time=50):
    row = [0]*(n)+[1]*(n)
    box = np.vstack([row]*m)
    x = np.arange(-0.5, 2*n, 1)
    y = np.arange(-0.5, m, 1)
    
    left_prop_list = []
    right_prop_list = []
    left_n=[]
    right_n=[]
    time_list = []
    
    t = 0
    while t < max_time:
        Z = box
        
        cutoff=n
        
        left = Z[:, 0:cutoff]
        right = Z[:, cutoff:2*n]
        
        prop_l=np.count_nonzero(left)/(m*n)
        prop_r=np.count_nonzero(right)/(m*n)
        
        left_n.append(np.count_nonzero(left))
        right_n.append(np.count_nonzero(right))
        
        left_prop_list.append(prop_l)
        right_prop_list.append(prop_r)
        time_list.append(t)
        
        
        fig, ax = plt.subplots()
        ax.pcolormesh(x, y, Z, cmap="plasma", edgecolors='k')
        plt.xlabel(("Time: {}".format(t)))
        plt.ylabel("{} x {} grids".format(n, m))
        plt.title("Left {} ; Right {}".format(round(prop_l,ndigits=3), round(prop_r,ndigits=3)))
        t += 1
        
        plt.plot([(cutoff-0.5), (cutoff-0.5)], [-0.5, m-0.5], 'r-', lw=4)
        plt.show() 
        
        for row in box:
            step_time(row)
    prop_dict = {"Time": time_list,
                 "Left Proportion" : left_prop_list,
                 "Right Proportion": right_prop_list,
                 "Left Number"     : left_n,
                 "Right Number"    : right_n}
    return pd.DataFrame(prop_dict)

def exchange_no_plot(n=10, m=8, max_time=50):
    row = [0]*n+[1]*n
    box = np.vstack([row]*m)
    
    left_prop_list = []
    right_prop_list = []
    left_n=[]
    right_n=[]
    time_list = []
    
    t = 0
    while t < max_time:
        Z = box
        
        left = Z[:, 0:n]
        right = Z[:, n:2*n]
        
        prop_l=np.count_nonzero(left)/(m*n)
        prop_r=np.count_nonzero(right)/(m*n)
        
        left_n.append(np.count_nonzero(left))
        right_n.append(np.count_nonzero(right))
        
        left_prop_list.append(prop_l)
        right_prop_list.append(prop_r)
        time_list.append(t)
        
        t += 1
        for row in box:
            step_time(row)
    prop_dict = {"Time": time_list,
                 "Left Proportion" : left_prop_list,
                 "Right Proportion": right_prop_list,
                 "Left Number"     : left_n,
                 "Right Number"    : right_n}
    return pd.DataFrame(prop_dict)


def compute_entropy(x_array):
    N = len(x_array)
    return -N*(x_array*np.log(x_array)+(1-x_array)*np.log(1-x_array))

def compute_actual_entropy(N, n_list):
    entropy_list = []
    fact = lambda x: np.math.factorial(x)
    for n in n_list:
            entropy_list.append(np.log((fact(N))/(fact(n)*fact(N-n))))
    return np.array(entropy_list)
        
def make_plots():
    
    legend_list = []    
    for i in [5, 9, 11, 15]:
        height = i
        length=i
        df = exchange_no_plot(n=length, m=height, max_time=200)

        entropy_left = compute_actual_entropy(length*height, df["Left Number"])
        entropy_right = compute_actual_entropy(length*height, df["Right Number"])
        legend_list.append("N={}".format(length*height))
        
        plt.plot(df["Time"], entropy_left + entropy_right)
        plt.xlabel("Time")
        plt.ylabel("Entropy (units of k)")
        plt.title("Entropy vs Time for the Thermal Contact Model")
    plt.legend(legend_list)
    plt.show()
    