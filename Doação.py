
acum_reais = 0
acum_vic = 0 
while True: 
    reais = float(input())
    if reais < 0: 
        break
    vic = reais * 2.5
    print(f'Tantos vicoin{vic}')
    acum_reais += reais 
    acum_vic += vic
 
print(f'VC$ {acum_reais:.2f}')
print(f'R$ {acum_vic:.2f}') 
print(f'vic cois {vic}')