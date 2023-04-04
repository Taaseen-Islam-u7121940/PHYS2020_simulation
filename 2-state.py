"""
Module 2-state
Author: Taaseen Islam (u7121940)
This module contains code for models of a 2-state system"""

from vpython import *
from matplotlib import pyplot as plt
import numpy as np
import csv

#Initial values
m = 0.4027
g = 9.81
k= 12.1
l = 0.175

alpha=0
beta=0.01

angle_pos = radians(15.5)
angle_vel = 0
spring_pos = 0.32
spring_vel = 0

r=l+spring_pos

#Items
spring = helix(pos=vec(0,0,0), axis=vec(r*sin(angle_pos),-r*cos(angle_pos),0), 
               radius=0.008, coils = 50, thickness=0.008)
mass = box(pos=vec(r*sin(angle_pos),-r*cos(angle_pos),0), 
           size=vec(0.05,0.05,0.01), color=color.yellow)
metrestick = box(pos=vec(0,-0.5,0), size=vec(0.01,1,0.01), color=color.cyan)
stick_label = label(pos = vec(0.1,-0.95,0), text="1 m")

tlist=[]
springlist=[]
anglelist=[]
rlist=[]
xlist=[]
ylist=[]
t=0
dt=0.01
while t<10:
    rate(100)
    
    angle_acc =(-g*sin(angle_pos)-2*spring_vel*angle_vel)/r - (alpha/m)*angle_vel 
    spring_acc = (g*m*cos(angle_pos)-k*spring_pos+m*(l+spring_pos)*angle_vel**2)/m \
        - (beta/m)*spring_vel
    angle_vel =  angle_vel +  angle_acc*dt
    
    angle_pos = (angle_pos + angle_vel*dt)
    spring_vel = spring_vel + spring_acc*dt
    spring_pos = (spring_pos + spring_vel*dt)
    r=l+spring_pos
    
    mass.pos=vec(r*sin(angle_pos),-r*cos(angle_pos),0)
    spring.axis=mass.pos
    
    tlist.append(t)
    springlist.append(spring_pos)
    anglelist.append(degrees(angle_pos))
    rlist.append(r)
    xlist.append(r*sin(angle_pos))
    ylist.append(-r*cos(angle_pos))
    t += dt 

plt.plot(tlist, rlist)