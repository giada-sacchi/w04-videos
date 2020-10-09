import numpy
import matplotlib.pyplot as plt

### ALGEBRAIC CONTEXT

m1 = 0.5
b1 = 0.5
m2 = -1
b2 = 2

A = numpy.array([[-m1, 1], [-m2, 1]])
b = numpy.array([[b1], [b2]])

Ainv = numpy.linalg.inv(A)
print(Ainv)

#print(numpy.dot(Ainv, b))  #WRONG!
#print(Ainv*b)

print(numpy.linalg.solve(A, b))

###PLOT

x_1 = numpy.linspace(-2, 6, 121)
y_1 = m1*x_1 + b1

x_2 = x_1
y_2 = m2*x_2 + b2

plt.plot(x_1, y_1, color='magenta', linewidth=3)
plt.plot(x_2, y_2, linestyle='--')

plt.legend(['y = 0.5x + 0.5', 'y = -x + 2'])
plt.grid()
plt.show()

# The intersection is at (1,1) as expected
