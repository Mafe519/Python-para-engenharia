#Exemplo de derivadas com o sympy

import sympy as sp

x = sp.symbols('x')
f = x**2 + 4*x + 3
derivada = sp.diff(f, x)

#sp.solve(expr,var) resolve equações
#sp. simplify e expand para simplificar e expandir equações 

print("Derivada de x²:", derivada)
