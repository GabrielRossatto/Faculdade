l = []
c = 0

while c == 0:
    t = int(input())
    if t > 0:
        l.append(t)
    else:
        c = 1
media= sum(l)/len(l)

print(f'MEDIA: {media:.2f}')
for i in l:
    if i < media:
        print(f'{i}')  