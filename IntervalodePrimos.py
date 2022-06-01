start = int(input())
end = int(input())
cont = 0
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 
        cont += 1
print(f'primos: {cont}')