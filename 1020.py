dias = int(input())

anos = dias//365
dias = dias%365
mes  = dias//30
dias = dias%30

print(F'{anos} ano(s)\n{mes} mes(es)\n{dias} dia(s)')