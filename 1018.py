notas = int(input())
print(f'{notas}')

cem = notas//100
notas   = notas%100

cinquenta = notas//50
notas = notas%50

vinte = notas//20
notas   = notas%20

dez = notas//10
notas = notas%10

cinco = notas//5
notas = notas%5

dois = notas//2
notas= notas%2

print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{notas} nota(s) de R$ 1,00')