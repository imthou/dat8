"""
Implements matrix linear regression using NumPy, using
  the same packing crate example as before. Note the
  difference in storing the X data, since X is now a matrix
  instead of a vector.

To solve for the model parameters B:
	B = ((X'X)^-1)X'Y

To make predictions Y:
	Y = XB

Suppose there are n data points and k features. Then:
+ X: nxk matrix. Each row is a data point and each column is a feature.
+ B: kx1 row vector. Each row is the parameter corresponding to its feature in X.
     (i.e. with each unit increase in the feature, how much does y change?)
+ Y: nx1 column vector. Each row is the target of the corresponding X row.
     (XB = Y. Note that the matrix dimensions match: (nxk)*(kx1) = nx1.)

+ ^-1: matrix inverse.
+ ': matrix transpose.

Useful references:
  + https://codebright.wordpress.com/2011/10/07/linear-algebra-review-and-numpy/
  + http://isites.harvard.edu/fs/docs/icb.topic515975.files/OLSDerivation.pdf
    (see pages 8-11)
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def matrix_multiply(A, B): 
	"""Using NumPy, multiplies two matrices."""

    return np.array([])


def matrix_invert(A): 
	"""Returns the inverse of a matrix as a numpy array. 
	   If the matrix given is not invertible, this function 
	   returns the pseudoinverse of the matrix."""

    try: 
        return np.linalg.inv(A)
    except: 
        return np.linalg.pinv(A)


# 
def solve(X, y):
	"""Given matrix X and target vector y, finds the 
	   optimal parameters using linear regression.
	   B = ((X'X)^-1)X'Y. """
    
    # Remember to amend X to include the bias term! 
    
    return np.array([])



def get_predictions(b, test_set_X):
	"""Using the linear regression model, returns vector of y predictions,
	   given a vector of parameters b and a matrix of features X.
	   Y = XB. """

	# Optional to write -- it is not used below.

    return np.array([])


if __name__ == "__main__":
	# Time required -- note that each element is a vector of features.
	#   E.g., to represent two-dimensional features:
	#         [[10.15, 1.5], [2.96, 8.7], ...]
	X = np.array([[10.15], [2.96], [3.00], [6.88], [0.28], 
	              [5.06], [9.14], [11.86], [11.69], [6.04], 
	              [7.57], [1.74], [9.38], [0.16], [1.84]])

	# Total cases packed
	y = np.array([24, 6, 8, 17, 2, 
		          13, 23, 30, 28, 14, 
		          19, 4, 24, 1, 5])

	b = solve(X, y)

	print('Linear regression parameters: ', b)

	plt.cla()         # CLear All
	plt.hold(True)    # display each graph on top of the other
	plt.scatter([pt[0] for pt in X], y, color='r', marker='o')      # X, Y

	# this plots lines between the points (0,0) and (max(time), alpha*max(time))
	plt.plot([0, max(y)], [0, b[0] + b[1] * max(y)])
	plt.xlabel('Time (min)')
	plt.ylabel('Cases Packed')
	plt.title('Cases vs Time')

