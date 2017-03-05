# -----------------------------------------------------------------------------
# calculator.py
# Revised Function: 4 function calls in 0.021 seconds
# Original Function: 1000014 function calls in 2.849 seconds
# improvement index = 2.849/0.021 = 135.6666
# ----------------------------------------------------------------------------- 
import numpy as np
"""
Original Function:
Timer unit: 4.27654e-07 s
Total time: 4.33689 s
File: C:\Spring_2017\advpy\zl1732_assignment3\calculator_orig.py
Function: hypotenuse at line 45

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    45                                           def hypotenuse(x,y):
    46                                               
    47                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    48                                               x and y must be two-dimensional arrays of the same shape.
    49                                               
    50         1      2894435 2894435.0     28.5      xx = multiply(x,x)
    51         1      2546701 2546701.0     25.1      yy = multiply(y,y)
    52         1      2469497 2469497.0     24.4      zz = add(xx, yy)
    53         1      2230493 2230493.0     22.0      return sqrt(zz)
"""

"""
Revised Function
Timer unit: 4.27654e-07 s

Total time: 0.0182142 s
File: C:\Spring_2017\advpy\zl1732_assignment3\calculator.py
Function: hypotenuse at line 46

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    46                                           def hypotenuse(x,y):
    47                                               
    48                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    49                                               x and y must be two-dimensional arrays of the same shape.
    50                                               
    51         1        10633  10633.0     25.0      xx = np.multiply(x,x)
    52         1        10946  10946.0     25.7      yy = np.multiply(y,y)
    53         1         8978   8978.0     21.1      zz = np.add(xx, yy)
    54         1        12034  12034.0     28.3      return np.sqrt(zz)
"""





"""
def add(x,y):

    Add two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.

    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = x[i,j] + y[i,j]
    return z
"""
"""
def multiply(x,y):

    Multiply two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.

    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = x[i,j] * y[i,j]
    return z
"""
"""
def sqrt(x):

    Take the square root of the elements of an arrays using a Python loop.

    from math import sqrt
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = sqrt(x[i,j])
    return z
"""

def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = np.multiply(x,x)
    yy = np.multiply(y,y)
    zz = np.add(xx, yy)
    return np.sqrt(zz)