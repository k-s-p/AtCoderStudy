#区間DPの考えで解けます
#𝑴𝒊×𝑴(𝒊+1)の乗算数は、𝑟𝑖×𝑟(𝑖+1)×𝑟(𝑖+2)になります。
INF = 10**10
N = int(input())
dp = [[INF]*N for _ in range(N)]
R = []
for n in range(N):
    r, c = map(int,input().split())
    R.append(r)
R.append(c)

for i in range(N):
    dp[i][i] = 0 # 対角成分すなわち、行列積Miを計算するコストは0である

for l in range(1,N): # iとjの差分
    for i in range(N-l):
        j = i+l    
        for k in range(i,j):
            # cost(左側行列積) + cost(右側行列積) + 行列計算のコスト
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+R[i]*R[k+1]*R[j+1]) # 初回はR[0]*R[1]*R[2]
print (dp[0][-1])