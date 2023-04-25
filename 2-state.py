"""
Module 2-state
Author: Taaseen Islam (u7121940)
This module contains code for statistical models of a 2-state system

Current code: rudimentary simulation of essentially flipping a coin"""

import random
from matplotlib import pyplot as plt

prop_list = []
num_trials = 500
num_objects = 20
for trial in range(num_trials):
    obj_list = []
    for i in range(num_objects):
        obj_list.append(random.randint(0, 1))
    
    proportion = len(list(filter(lambda x: x==1, obj_list)))/len(obj_list)
    prop_list.append(proportion)
    
plt.hist(prop_list, density=True)
