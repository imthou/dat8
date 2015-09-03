
""" 
# DAT-LA-08: Homework 1
#
# Linear Regression
#
# Uppercase single letters indicate vectors.
# Lowercase single letters indicate scalars.
"""

import os
from matplotlib import pyplot as plt

# Points for testing.
# Consists of the two points: [(0, 2), (1, 4)]
# What do you expect to get for m and b?
X_test = [0, 1]
Y_test = [2, 4]

# Homework data. What are m and b?
# Consists of the points: [(15.52, 19.93), (4.10, 3.55), ...]
X = [15.52, 4.10, 64.47, 11.71, 99.21, 
     30.75, 41.15, 38.15, 3.69, 94.28]

Y = [19.93, 3.55, 56.73, 10.67, 81.99, 
     36.74, 38.14, 30.52, 7.60, 96.54]


def plot_model(X, Y, m, b):
	""" Draw scatter plot of data points and
		the predicted line y = mx + b. """
	plt.scatter(X, Y, color='r')
	plt.plot(
		(min(X),max(X)), 
		(m*min(X) + b, m*max(X) + b), 
		color='b')
	plt.title('Best fit line')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('out.png')
	print('Saved figure to {}'
		.format(os.path.dirname(os.path.realpath(__file__)) + 
				'/out.png'))


def mean(nums):
	""" Returns mean value of nums. """
	return 1.0


def intercept(X, Y, m):
	""" Given data points (xi, yi) and slope m, 
		returns the y-intercept of the best-fit line. """
	return 1.0


def slope(X, Y):
	""" Given data points (xi, yi), returns
	    the slope m of the best-fit line. """

	return 1.0


# TEST the mean function
print("mean([0, 1]) => ", mean(X_test))
print("mean([2, 4]) => ", mean(Y_test))

# More tests
#
#
#

# Test linear regression on points: [(0, 2), (1, 4)]
m = slope(X_test, Y_test)
b = intercept(X_test, Y_test, m)
plot_model(X_test, Y_test, m, b)

# Fit and plot model for actual X and Y
#
#
#

print()
print("Slope (m): {}".format(m))
print("Intercept (b): {}".format(b))
print("Model: y = {}x + {}".format(m, b))
