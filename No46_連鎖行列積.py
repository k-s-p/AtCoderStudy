#区間DPの考えで解けます
#連鎖行列は、左の行数*左の列数*右の列数。
INF = 10**10
N = int(input())
dp = [[INF]*N for _ in range(N)]
R = []
for n in range(N):
    r, c = map(int,input().split())
    R.append(r)
R.append(c) #一番左の行数と各列の列数が分かれば連鎖行列積を計算可能
#print(R)

for i in range(N):
    dp[i][i] = 0 # 対角成分すなわち、行列積Miを計算するコストは0である

#dp[i][j] = 区間[i,j)までの最小の行列積の計算コスト
for l in range(1,N): #iとjの差分
    for i in range(N-l): #iは最初大きい
        j = i+l
        for k in range(i, j):
            #[i, k)までのcostと[k+1,j)のコストと行列計算のコスト
            #行列の掛け算の結果の行列は左の行数と右の列数を持つ行列である
            #つまり、iの行数、kの列数,jの列数をかければコストがでる
            #dp[i][k] = 既に計算されている左側行列の計算コスト
            #dp[k+1][j] = 既に計算されている右側行列の計算コスト
            tmp = dp[i][k] + dp[k+1][j] + R[i]*R[k+1]*R[j+1]
            dp[i][j] = min(dp[i][j], tmp)
            
print(dp[0][-1])