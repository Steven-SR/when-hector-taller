def rotate(X,n):
    temp=X.copy()
    for _ in range(n):
        temp=flip(transpose(temp))
    if n>4:
        return flip(temp)
    return temp
def transpose(A):
    return [[A[j][i] for j in range(len(A[0]))]for i in range (len(A))]
def flip(A):
    for i in A:
        i=i.reverse()
    return A
X= [['&','&','.','.'],
    ['&','&','.','.'],
    ['&','.','.','.'],
    ['.','.','.','.']]

print(rotate(X,8))