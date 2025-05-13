import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
f = x**3 + 5*x**2 + 3*x
g = 3*x**2 + 10*x + 3
h = 6*x + 10

fig, aux = plt.subplots()
aux.plot(x, f, color="red", label= "f(x)")
aux.plot(x, g, color="orange", label= "g(x)")
aux.plot(x, h, color="black", label= "h(x)")

aux.set_xlabel('x')
aux.set_ylabel('y')
aux.legend()

plt.show()