total = int(input())
pag = int(input())
i = 1
for c in range(total, 0, -pag): 
    print(f'pagamento: {i}')
    print(f'antes = {c}')
    depois = c - pag
    if c < pag: 
        depois = c - c 
        print(f'depois = {depois}')
    else: 
        print(f'depois = {depois}')
    i += 1  
    print('-----')
    