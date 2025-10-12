# cook your dish here
N = int(input())
lst = []
for alpha in range(N):
    (a, b, c) = (map(int, input().split(' ')))
    if a>b and a>c:
        if b>c:
            print(b)
        else: print(c)
    elif b>a and b>c:
        if a>c:
            print(a)
        else: print(c)
    elif a>b:
        print(a)
    else: print(b)