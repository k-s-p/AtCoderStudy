#先に10^6までのすべての解を求めておく
#dp[i] = iを表すのに必要な正四面体の数
#正四面体数pとおくと、dp[i+p] = dp[i]+1 or dp[i+p
#2変数のminを使うより、ifで比較したほうが速い

def main():
    ans = []
    N = 10**6
    dp = [10**10]*(N+1)
    dp_odd = [10**10]*(N+1)
    dp[0] = 0
    dp_odd[0] = 0

    for n in range(N+1):
        p = n*(n+1)*(n+2) // 6 #n番目の正四面体数
        if p >= N:
            break
        for i in range(N-p): #i+pがN以下まで
            #dp[i+p] = min(dp[i+p], dp[i] + 1)
            new = dp[i]+1
            if dp[i+p] > new:
                dp[i+p] = new
        
        #奇数の正四面体数のとき、その和の最小を保持
        if p%2 == 1:
            for i in range(N-p): #i+pがN以下まで
                #dp_odd[i+p] = min(dp_odd[i+p], dp_odd[i] + 1) 
                new = dp_odd[i]+1
                if dp_odd[i+p] > new:
                    dp_odd[i+p] = new 
    
    while True:
        a = int(input())
        if a == 0:
            break
        ans.append([dp[a], dp_odd[a]])

    for a, b in ans:
        print(a,b)


if __name__ == '__main__':
    main()
