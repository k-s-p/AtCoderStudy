def solve(a, b):
    lx, ly = len(a),len(b)
    #DPの要素DP[i]は、Xを左からi文字切り出した部分列とYを左からj文字切り出した部分文字列の共通部分長
    dp = [0 for i in range(ly+1)]

    for i in range(lx):
        mem = dp[:]
        for j in range(ly):
            if a[i] == b[j]:
                dp[j+1] = mem[j] + 1
            elif dp[j] > dp[j+1]:
                dp[j+1] = dp[j]
    print(dp[ly])
    return 

q = int(input())

for _ in range(q):
    X = input()
    Y = input()
    
    solve(X,Y)
