#DPで解ける
#i番目までで作れる0~20の数字を記録すると解けるらしい

N = int(input())
Num = list(map(int, input().split()))

dp = [[0 for i in range(21)] for j in range(N+1)]
dp[1][Num[0]] = 1
# print(dp)
for i in range(1, N):
    for j in range(21):
        plus = j + Num[i] #i番目の値に＋記号をつけたときにできる数値
        minus = j - Num[i] #i番目の値に-記号をつけたときにできる数値
        if plus >= 0 and plus <= 20:
            dp[i+1][plus] += dp[i][j] #i番目の値まででjを作れる数を,i+1番目の値でplusを作れる数に加える
        if minus >= 0 and minus <= 20:
            dp[i+1][minus] += dp[i][j]
    # print(dp[i])
print(dp[N-1][Num[N-1]]) #最後に、N-1番目の値で作れる,最後の数値の数がほしい答え