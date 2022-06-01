from math import sqrt 

x1, y1 = map(float, input().split(' '))
x2, y2 = map(float, input().split(' '))

formula = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'{formula:.4f}')