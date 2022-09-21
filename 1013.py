a,b,c = map(int, input().split(' '))

maiorAb = int((a+b+abs(a-b))/2)
maior = int((maiorAb+c+abs(maiorAb-c))/2)

print(f'{maior} eh o maior')