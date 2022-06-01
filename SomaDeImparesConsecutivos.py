x = int(input())
y = int(input())


soma = 0

if x > y:
    for c in range(x, y): 
        if c % 2 != 0: 
            soma += c
else:
    for c in range(y, x):
        if c % 2 != 0: 
            soma += c
print(soma)