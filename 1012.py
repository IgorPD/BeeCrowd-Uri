a,b,c = map(float, input().split(' '))
pi=3.14159

print(f'TRIANGULO: {(a*c)/2:.3f}')
print(f'CIRCULO: {(c**2)*pi:.3f}')
print(f'TRAPEZIO: {((a+b)*c) /2:.3f}')
print(f'QUADRADO: {b*b:.3f}')
print(f'RETANGULO: {a*b:.3f}')