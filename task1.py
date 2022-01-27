import sys


n = int(sys.argv[1])
m = int(sys.argv[2])
a = [i for i in range(1, n + 1)]
answer = '1'

if n != 0 and m != 0:
    i = (m - 1) % n
    while a[i] != 1:
        answer += str(a[i])
        i = ((i + m) - 1) % n

    print(answer)