num = int(input())
l = []
for i in range(1):
    if 1 <= num <= 999:
        for i in range(num):
            n1 = float(input())
            l.append([n1])
        

        for j in range(num):
            n2 = float(input())
            l[j].append(n2)
         

        alt = 0
        for c in range(num):
            if l[c][0] == 10:
                l[c].append(l[c][0])
                l[c].append('-')
                alt = alt + 0
                
            elif l[c][1] == 10:
                x = l[c][0] + 2
                if x > 10:
                    x = 10
                else:
                    x = x
                l[c].append(x)
                l[c].append('*')
                alt = alt + 1
            else:
                l[c].append(l[c][0])
                l[c].append('-')
                alt = alt + 0

        print(f'NOTAS ALTERADAS: {alt}')
        for w in range(num):
            print(f'{l[w][3]}({w+1:03}) original: {l[w][0]:05.2f} | final: {l[w][2]:05.2f}')
    
    else:
        break