#Exemplo com scipy para calcular integrais

from scipy.integrate import quad

f = lambda x: x**2 + 3*x + 3  # função f(x) = x
resultado, erro = quad(f, 0, 2)  # integra f(x) de 0 a 2

print("Integral de x de 0 a 2 =", resultado)
