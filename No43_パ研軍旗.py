# 左の列から順に評価する
# n列目の色がcであるとき、塗り替えの最小値をdp[n][c]として記録する
#つまり、各列を1色で塗り替えた場合の最小値を3色全てのパターン記録しておく
N = int(input())
S = []
col = {'R':0, 'B':1, 'W':2, '#':-1} #各色を数値に変換

for i in range(5):
    ls = list(input())
    ls = [-1] + [col[e] for e in ls] #一番左にダミーの列
    S.append(ls)

dp = [[0]*3 for i in range(N+1)]

#動的計画法で各列を各色で塗り替えたときの結果を計算
for n in range(1,N+1): #列
    for c in range(3): #色
        cnt = 0
        #色cで塗り替えるとどうなるかカウント
        for i in range(5):
            if S[i][n] != c:
                cnt += 1
        k = [0,1,2] #前の列の色
        k.remove(c) #前の列の内、同じ色の列を除外
        dp[n][c] = min(dp[n-1][k[0]] + cnt, dp[n-1][k[1]] + cnt)
        
print(min(dp[-1])) #最終列まで塗り替えたときの一番小さい塗り替えの数