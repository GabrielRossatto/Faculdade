from math import trunc

n = int(input())
lista = []

for i in range (n):
    info = input()
    l1 = [x for x in info.split(';')]
    lista.append(l1)    

x = float(input())
y = float(input())


for j in range(n):
    if lista[j][3] == 'sim':
        b = int(lista[j][1])
        if b >= 1000:
            lista[j].append(((trunc(b/1000)*x)))
        else:
            lista[j].append(0)
    
    elif lista[j][3] == 'não':
        b = int(lista[j][1])
        if b >= 1000:
            lista[j].append(((trunc(b/1000)*y)))
        else:
            lista[j].append(0)

print('-----')
print('BÔNUS')
print('-----')

for j in range(n):
    print(f'{lista[j][0]}: R$ {float(lista[j][4])+float(lista[j][2]):.2f}')  