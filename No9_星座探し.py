m = int(input())
A = [list(map(int,input().split())) for _ in range(m)]

n = int(input())
B = [list(map(int,input().split())) for _ in range(n)]

#移動量
x,y = 0,0
A.sort()
B.sort()
ans = []
for i in range(n):
    ok = 1
    x = B[i][0] - A[0][0]
    y = B[i][1] - A[0][1]

    k = i+1
    for j in range(1, m):
        while k < n:
            if A[j][0] + x == B[k][0] and A[j][1] + y == B[k][1]:
                ok += 1
                k += 1
                break
            k += 1
        if ok == len(A):
            break
    if ok == len(A):
        ans = [x,y]
print(*ans)