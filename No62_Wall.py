#ワ―シャルフロイド法で解ける
H,W = map(int, input().split())

#入力をdpテーブル扱いする
C = [list(map(int, input().split())) for i in range(10)]
INF = 0
for i in range(10):
    mx = max(C[i])
    if mx > INF:
        INF = mx
    
A = [list(map(int, input().split())) for i in range(H)]

#ワ―シャルフロイド
for k in range(10):
    for i in range(10):
        if C[i][k] == INF:
            continue
        for j in range(10):
            if C[k][j] == INF:
                continue
            C[i][j] = min(C[i][j], C[i][k] + C[k][j])

# for i in range(10):
#     print(*C[i])

#数値変換
ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] >= 0:
            ans += C[A[i][j]][1]

print(ans)