#ワ―シャルフロイドの応用で解ける
N = int(input())
INF = 10**10
C = [[INF] * N for i in range(N)]

for i in range(N):
    A = list(map(int, input().split()))
    for j in range(N):
        if i == j:
            continue
        C[i][j] = A[j]

#ワ―シャルフロイド
ans = 0
for k in range(N):
    for i in range(k+1, N):#i < j
        mn = INF
        for j in range(N): 
            mn = min(mn, C[i][j] + C[k][j])
        if mn < C[k][i]: #与えられた経路が最短経路ではない
            print(-1) #終了
            exit()
        if mn > C[k][i]: #等しくない場合は、u-vを結ぶ経路が必要
            ans += C[k][i]
print(ans)