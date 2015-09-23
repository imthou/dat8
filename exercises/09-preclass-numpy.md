##Pre-class: Numpy + Matrices

https://codebright.wordpress.com/2011/10/07/linear-algebra-review-and-numpy/


```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[1, 2], [3, 4], [5,6]])

```
1. What happens if you do `a * b`?
Check the help function of np.dot(). (run `help(np.dot())`)

2. Why does `a.dot(b)` fail? Why does `a.dot(c)` work?

3. Is `np.dot(a, c)` the same as `a.dot(c)`? Why or why not?

4. Is `np.dot(a, c)` the same as `np.dot(c, a)`? Why or why not?