
m,n,cant=input().split()
m=int(m)
n=int(n)
cant=int(cant)
final = []
for _ in range(cant):
    piz = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        line = input()
        for j in range(4):
            piz[i][j] = line[j]
    final.append(piz)


######test input
for xd in range(len(final)):
    print(final[1])
############################

