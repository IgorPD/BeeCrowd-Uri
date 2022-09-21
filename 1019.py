sec = int(input())

horas = sec//(60*60)
sec   = sec%(60*60)

minutos = sec//60
sec     = sec%60

print(f'{horas}:{minutos}:{sec}')