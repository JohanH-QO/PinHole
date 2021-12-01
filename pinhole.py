# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:56:45 2021

@author: Johan
"""

import numpy as np
import matplotlib.pyplot as plt

um = 1e-6
nm = 1e-9
mm = 1e-3

D = 50*um #pinhole diameter
wvl = 795*nm #wavelength
a = 2600*um #waist
Tot_pow = 0.200 #total power of beam
F = 250*mm #lense focale

P = Tot_pow*(1-np.exp(-0.5*((np.pi*a*D/(wvl*F))**2)))

print(P)
print(P/Tot_pow)

D2 = np.linspace(0,100*um,1000)
P2 = Tot_pow*(1-np.exp(-0.5*((np.pi*a*D2/(wvl*F))**2)))

plt.figure()
plt.plot(D2/um,P2/Tot_pow)
plt.xlabel('pinhole diameter (um)')
plt.ylabel('power transmitted')
