n = int(input())

for i in range (n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if b[0]>=a[0] and b[1]>=a[1]:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")