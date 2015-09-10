# -*- coding: utf-8 -*-
"""
  Basic regression through the origin.
"""

import numpy as np
import matplotlib.pyplot as plt

# Cases packed vs time
time = [10.15, 2.96, 3.00, 6.88, 0.28, 
        5.06, 9.14, 11.86, 11.69, 6.04, 
        7.57, 1.74, 9.38, 0.16, 1.84]

cases = [24, 6, 8, 17, 2, 
         13, 23, 30, 28, 14, 
         19, 4, 24, 1, 5]


def find_alpha(X, Y):
    """ 
    Using linear regression through the origin, 
      computes the alpha which minimizes the sum of square errors:
        y_pred = alpha * x

    Assumes we are given N data points, where len(X) == len(Y) == N
    """
    return 0.5


alpha = find_alpha(time, cases)

plt.cla()         # CLear All
plt.hold(True)    # display each graph on top of the other
plt.scatter(time, cases, color='r')      # X, Y

# this plots lines between the points (0,0) and (max(time), alpha*max(time))
plt.plot([0, max(time)], [0, alpha * max(time)], color='b')
plt.savefig('out.png')