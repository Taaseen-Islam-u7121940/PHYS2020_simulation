# -*- coding: utf-8 -*-
"""
Module: Einstein-Solid
Contains code for a model of an Einstein Solid

CURRENT CODE: Adapted from Malthe-Sorenssen, Dysthe 2017
https://www.uio.no/studier/emner/matnat/fys/FYS2160/h18/pensumliste/stat_thermal_phys_python.pdf
Chapter 6.3, Page 136
"""

# Einstein solid NA - NB multiplicity
import pylab as pl
from scipy.special import comb
import pandas as pd
NA = 100
NB = 100
q = 200
N = NA + NB
# Find multiplicity of all macrostates
omegaA = pl.zeros(q+1)
qAvalue = pl.zeros(q+1)
omegaB = pl.zeros(q+1)
omegaAB = pl.zeros(q+1)
# Loop through all macrostates and find multiplicity
for istate in range(0,q):
    qA = istate
    qAvalue[istate] = qA
    omegaA[istate] = comb(qA+NA-1,qA)
    qB = q - qA
    omegaB[istate] = comb(qB+NB-1,qB);
    omegaAB[istate] = omegaA[istate]*omegaB[istate];
SA = pl.log(omegaA)
SB = pl.log(omegaB)
SAB = pl.log(omegaAB)
pl.plot(qAvalue,SAB, '-o')
pl.xlabel('q'),pl.ylabel('W')
pl.show()
#Log all multiplicities
mult_matrix = [omegaA, omegaB, omegaAB]
s_matrix    = [SA, SB, SAB]
#Create a dataframe of multiplicities;
#Columns are the number of units of q in A
#Rows are multiplicity of A, multiplicity of B, multiplicity of both
mult_df = pd.DataFrame(mult_matrix, index=["A", "B", "AB"])
s_df = pd.DataFrame(s_matrix, index=["A", "B", "AB"])