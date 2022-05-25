#すべての風船を高度xまでで割れるかどうかで二分探索することができる。
#これにより、xまでで割れる、割れないの境界値を探索することができるから。
#例えば、xが100までですべての風船が割れるならそれ以降のx,例えば200でもすべて割れることがわかる。

N = int(input())
H = []
S = []
for i in range(N):
    h,s = map(int, input().split())
    H.append(h)
    S.append(s)

#二分探索
ng = 0
ok = 1e+14
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    
    #すべて割れるかの判定
    judge = True
    ls = [0] * N
    for i in range(N):
        #風船が高度xに達するまでの時間(何秒以内に割るべきか)
        if mid < H[i]: #そもそも風船の初期高度がmidより高いならfalse
            judge = False
        else:
            ls[i] = (mid-H[i])//S[i]
    
    #制限時間順にソート
    ls.sort()
    for i in range(N):
        if ls[i] < i: #時間切れが発生
            judge = False
    
    if judge:
        ok = mid
    else:
        ng = mid
    
print(int(ok))