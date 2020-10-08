# %% md
# Let's consider two lines expressed as: <br />
# $y = m_1 x + b_1$, $y = m_2 x + b_2$ <br />
# We can do this by form the matrix A and b: <br />
#  $ A = \begin{bmatrix}
#  -m_1 & 1\\
#  -m_2 & 1
# \end{bmatrix} $,
#  $ b = \begin{bmatrix}
#  b_1\\
#  b_2
# \end{bmatrix},
# X = \begin{bmatrix}
#  x\\
#  y
# \end{bmatrix} $ <br />
# $A X = b$ <br />
# And then calculate
# $\begin{bmatrix}
#  x^*\\
#  y^*
# \end{bmatrix} = A^{-1} b $,<br />
# where $(x^*,y^*)$ the intersection coordinate


# %% codecell

import numpy
import matplotlib.pyplot as plt


m1 = 0.5
b1 = 0.5
m2 = -1
b2 = 2

A = numpy.array([[-m1, 1], [-m2, 1]])
b = numpy.array([[b1], [b2]])

Ainv = numpy.linalg.inv(A)


# print(numpy.dot(Ainv, b))

x_1 = numpy.linspace(-2, 6, 121)
y_1 = m1*x_1 + b1

x_2 = x_1
y_2 = m2*x_2 + b2

plt.plot(x_1, y_1, color='magenta', linewidth=3)
plt.plot(x_2, y_2, linestyle='--')

plt.legend(['y = 0.5x + 0.5', 'y = -x + 2'])
plt.grid()
plt.show()
