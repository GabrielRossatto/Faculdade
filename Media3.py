"""n1, n2, n3, n4 = map(float, input().split(' '))

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10


print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')

if media < 5:
    print('Aluno reprovado.')

elif media >= 5 and media <= 6.9: 
    print('Aluno em exame.')
    ne = float(input())
    print(f'Nota do exame: {ne:.1f}')
    media = (media + ne) / 2

    if media >= 5: 
        print('Aluno aprovado.')
         
    else: 
        print('Aluno reprovado')
    print(f'Media final: {media:.1f}') 


    

# 4 + 19,5 + 16 + 9 """
a = 5
b = 4
c = 9
d = 7
e = 1
f = 2
s = 10
s += a + b ** (c - d) / e * f

print(s)
