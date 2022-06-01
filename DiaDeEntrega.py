calendario = ['domingo', 'segunda', 'terca', 
             'quarta', 'quinta','sexta','sabado']

dia = str(input())
qtd_dia = int(input())

for c in range(0, 7): 
    if dia == calendario[c]:
        sum = c + qtd_dia
        if qtd_dia == 0: 
            print('chega hoje!')
        elif sum >= 6:
            total = sum - 7 
            print('sera entregue', calendario[total])
        else: 
            print('sera entregue', calendario[sum])




            

        