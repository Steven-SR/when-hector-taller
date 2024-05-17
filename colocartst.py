final=[]
final.append([['+', '+', '+', '+'], ['+', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']])
final.append([['*', '.', '.', '.'], ['*', '.', '.', '.'], ['*', '*', '*', '.'], ['.', '.', '.', '.']])
final.append([['#', '.', '.', '.'], ['#', '#', '#', '.'], ['#', '.', '.', '.'], ['.', '.', '.', '.']])

piz = [["." for _ in range(6)] for _ in range(5)]

def move(T,pizT,i,j):
    newT=T
    piz=cropM(pizT)
    for oi  in range(len(piz)):
        for oj in range(len(piz[0])):
            if oi+i >= len(newT) or oj+j >= len(newT[0]) or newT[oi+i][oj+j] != ".":
                return T,False
            newT[oi+i][oj+j] = piz[oi][oj]
    return newT,True

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


def call(Tab,final):
    while final:
        actPiz=final.pop()
        for i in range (len(Tab)):
            for j in range (len(Tab[0])):
                newTab,stat=move(piz,actPiz,i,j)
                if stat:
                    print(final)
                    call(newTab,final)
    return Tab

#Tab esta devolviendo una combinacion rara hasta cierto punto, final parece funcionar bien


print(call(piz,final))
