def mostrar():
    carrinho.sort()
    return print(*carrinho, sep=' ')

def add(a):
    carrinho.append(a)


def remover(a):
    try:
        carrinho.remove(a)
    except:
        print(f'código {a} não encontrado')

carrinho = []
n = 0

while n == 0:
    opc = input()
     
    if opc == '': 
        pass
    elif opc == 'encerrar':
        n = 1
        mostrar()
        car = []

    else:
        car = [int(x) for x in opc.split()]
        for x in car:
            add(x)
        car = []
    
    while n == 0:
        opc = input()
        car = [x for x in opc.split()]         
        
        if opc == 'exibir':
            mostrar()
        
        elif opc == 'encerrar':
            n = 1
            mostrar()    
            car = []
        
        elif car[0] == 'adicionar':
            add(int(car[1]))
            car = []
        
        elif car[0] == 'remover':
            remover(int(car[1]))
            car = []