import sys


f1 = open(sys.argv[1], 'r')
rx, ry = map(float, f1.readline().split())
r = float(f1.readline())
f1.close()

a = []
f2 = open(sys.argv[2], 'r')
for line in f2:
    x, y = map(float, line.split())
    a.append([x, y])
f2.close()

for i in a:
    d = ((i[0] - rx)**2 + (i[1] - ry)**2)**0.5
    if d == r:
        print(0, end='\n')
    elif d < r:
        print(1, end='\n')
    else:
        print(2, end='\n')
