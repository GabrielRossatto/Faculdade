

qtd = int(input())
acum = 1

if qtd == 1:
    print(chr(65))
else: 
    print(chr(65))
    for c in range(66, 65 + qtd):
            acum += 1
            print(chr(c) * acum)