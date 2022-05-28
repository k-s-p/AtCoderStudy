#No35と違い、同じものをいくつでも選ぶことができる
#つまり、自分の行の過去データも使う
#dpの典型問題

N,W = map(int, input().split())
im = [list(map(int, input().split())) for i in range(N)]

#縦に品物をえらぶかどうか、横に重さを持つdpテーブルに価値を書き込んでいく
dp = [[0] * (W+1) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        if j < im[i-1][1]:
            dp[i][j] = dp[i-1][j]
        else:
            #品物iを選ばなかったときと、選んだときの価値が大きいほう
            #ひとつ前と行の同じ列と、同じ行の品物iの重さ分ひいた価値を比べる
            dp[i][j] = max(dp[i-1][j], dp[i][j-im[i-1][1]] + im[i-1][0])

print(dp[N][W])