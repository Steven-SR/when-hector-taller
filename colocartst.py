final=[]
final.append([['+', '+', '+', '+'], ['+', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']])
final.append([['*', '.', '.', '.'], ['*', '.', '.', '.'], ['*', '*', '*', '.'], ['.', '.', '.', '.']])

piz = [["." for _ in range(6)] for _ in range(5)]

def move(T,piz,i,j):
    for oi  in range(len(piz)):
        for oj in range(len(piz[0])):
            T[oi+i][oj+j] = piz[oi][oj]
    return T  

def cropM(M):
    Mempty = []
    Mtrans= []

    for fila in M:
        if not all(dotn == '.' for dotn in fila):
            Mempty.append(fila)

    for j in range(len(Mempty[0])):
        columna = [Mempty[i][j] for i in range(len(Mempty))]
        if not all(dotn == '.' for dotn in columna):
            Mtrans.append(columna)

    res = []
    for j in range(len(Mtrans[0])):
        fila = [Mtrans[i][j] for i in range(len(Mtrans))]
        res.append(fila)

    return res


h=move(piz,cropM(final[0]),2,2)
for i in h:
    print(i)
