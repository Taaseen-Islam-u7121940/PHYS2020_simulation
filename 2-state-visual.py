# -*- coding: utf-8 -*-
"""
Module 2-state Visual
Author: Taaseen Islam (u7121940)
This module contains code for visual models of a 2-state system

Current code: a yellow/purple grid of a two state system to show the probability
of less-likely microstates decreasing as N increases
"""
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np
from vpython import rate

#Sets length of the grid's axes and thus the number of objects N
length = 100
num_objs = length**2
#Creates grid of 1s and 0s
Z = np.random.randint(2, size=(length, length))
x = np.arange(-0.5, length, 1)  # len = 5
y = np.arange(-0.5, length, 1)  # len = 5

prop = np.count_nonzero(Z)/num_objs # Proportion of 1s

fig, ax = plt.subplots()
plt.title("{} Objects".format(num_objs))
plt.xlabel("Proportion: {}".format(round(prop, ndigits=3)))
ax.pcolormesh(x, y, Z)

''' Loop for viewing multiple graphs in succession.
time = 0
while time < 100:
    Z = np.rint(np.random.rand(length, length))
 #   prop = np.count_nonzero(Z)/num_objs

    fig, ax = plt.subplots()
    plt.title("{} Objects".format(num_objs))
  #  plt.xlabel("Proportion: {}".format(round(prop, ndigits=2)))
    ax.pcolormesh(x, y, Z)
    time += 1
    '''