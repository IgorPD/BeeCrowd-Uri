#1001
a = int(input())
b = int(input())
X = a + b

print('X = {}'.format(X))

print('X = {f''}')

#Não estava colocando o int nas variáveis para o uri realizar a conversão do arquivo
#O método format() em python serve basicamente para criar uma string que contém campos entre chaves que são substituidos pelos argumentos de format.

a = int(input())
b = int(input())
X = a + b

print(F'X = {X}')
#Maneira eficiente de usar Fstring


#1002
raio = float(input())
n    = 3.14159
area = n*(raio**2)

print(F"A={area:.4f}")

#Nesse exercício eu não tinha colocado o :.4f dentro do print
#para o output exibir 4 casas depois da vírgula

#1003
A = int(input())
B = int(input())
SOMA = A + B
print(F'SOMA = {SOMA}')


#1004
A = int(input())
B = int(input())
PROD = A * B
print(F'PROD = {PROD}')


#1005
N1 = float(input())
N2 = float(input())

MEDIA = (3.5*N1 + 7.5*N2)/11
print(f'MEDIA = {MEDIA:.5f}')


#1006
N1 = float(input())
N2 = float(input())
N3 = float(input())
MEDIA = (N1*2 + N2*3 + N3*5)/10
print(f'MEDIA = {MEDIA:.1f}')

#one line
print(f'media={(float(input())*2 + float(input())*3 + float(input())*5)/10}')

#1007
print(f'DIFERENCA = {(int (input()) * int (input()))-(int (input()) * int (input()))}')


#1008 TODO DIMINUIR ESTE CÓDIGO
NUMERO = int(input())
HORASTRAB = int(input())
VALORHR   = float(input())
SALARY = HORASTRAB * VALORHR

print(f'NUMBER = {NUMERO}\nSALARY = U$ {SALARY:.2f}')

#1009
nome    = str(input())
sal     = float(input())
totalv  = float(input())
total = (totalv * 0.15) + sal

print("TOTAL = R$ %.2f" % total)