# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 17:31:25 2025

@author: jacer352
"""

import numpy as np
import scipy.constants as const


def mirror_B_field(x, y, z):
    """Slab model of a magnetic mirror."""
    
    # Magnetic field from 4 parallell condictors in the z-direction
    I = 5e6
    I1 = I
    I2 = -I
    I3 = I
    I4 = -I
    
    x1, y1 = 1.0, 0.2
    x2, y2 = 1.0, -0.2
    x3, y3 = -1.0, 0.2
    x4, y4 = -1.0, -0.2
    
    Bx1, By1 = conductor_B_field(I1, x1, y1, x, y)
    Bx2, By2 = conductor_B_field(I2, x2, y2, x, y)
    Bx3, By3 = conductor_B_field(I3, x3, y3, x, y)
    Bx4, By4 = conductor_B_field(I4, x4, y4, x, y)

    Bx = Bx1 + Bx2 + Bx3 + Bx4
    By = By1 + By2 + By3 + By4
    Bz = 0.0
    
    return Bx, By, Bz


def conductor_B_field(I, x0, y0, x, y):
    """Evaluate B-field from straight conductor in z-direction."""
    
    d = np.sqrt((x-x0)**2 + (y-y0)**2)
    B = const.mu_0 * I / (2*np.pi * d)
    
    theta = np.arctan2(y-y0, x-x0)
    Bx = -B*np.sin(theta)
    By = B*np.cos(theta)
    
    return Bx, By
    