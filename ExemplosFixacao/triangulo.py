a = float(input('Primeiro lado: '))
b = float(input('segundo lado: '))
c = float(input('terceiro lado: '))

if(a + b < c) or (a + c < b) or (b + c < a):
    print('Não é triangulo!')
elif ( a==b ) and (a == c):
    print('Equilatero')
elif (a == b) or (a == c) or (b == c):
    print('Isósceles')
else:
    print('escaleno')