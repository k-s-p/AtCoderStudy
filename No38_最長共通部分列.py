def solve(a, b):
    lx, ly = len(a),len(b)
    #DPの要素DP[i][j]は、Xを左からi文字切り出した部分列とYを左からj文字切り出した部分文字列の共通部分長
    dp = [[0]*(ly+1) for i in range(lx+1)]

    for i, x in enumerate(a, 1):
        for j, y in enumerate(b, 1):
            if x == y:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[lx][ly])
    return 

q = int(input())

for _ in range(q):
    X = input()
    Y = input()
    
    solve(X,Y)
