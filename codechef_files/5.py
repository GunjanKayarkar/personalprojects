N = int(input())
counteven = 0
countodd = 0
#for alpha in range(N):
x = list(map(int, input().split()))
for bravo in range(len(x)):
    if x[bravo] % 2 == 0:
        counteven = counteven + 1
    else:
        countodd = countodd + 1
if counteven > countodd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")