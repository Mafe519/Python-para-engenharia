a, b = 0, 1 

num = int(input('quantos números da sequencia deseja ver? '))

for i in range(num):
    print(a)
    a, b = b, (a+b)