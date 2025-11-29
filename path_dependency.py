# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 05:10:38 2025

@author: asgun
"""

import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(0, 100, 100)

plt.figure(figsize=(10,6))

for i in range(12):

    y = x*(i-6) + np.random.normal(0, 30, size=x.shape)
    plt.plot(x,y, color = 'lightgray', linestyle='--')

y = x + np.random.normal(0, 30, size=x.shape)

plt.plot(x,y, color = 'green', linestyle='-', linewidth=2)

plt.show()