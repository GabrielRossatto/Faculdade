valores = (int(input()), int(input()), int(input()), int(input()), int(input()))

pares = 0
for c in range(len(valores)): 
    if valores[c] % 2 == 0: 
        pares += 1 
print(pares, ' valores pares')

