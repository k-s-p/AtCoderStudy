#bit全探索
N,M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

#N個のスイッチの全パターンを試す
ans = 0
for bit in range(1 << N):
    ok = True
    #print(bin(bit))
    for i,s in enumerate(S): #各電球の数だけループ
        cnt = 0
        for j in range(1, len(s)): #各スイッチが押されてるかの判定
            #print('1 << s[j]:',bin(1 << s[j]-1))
            if bit & (1 << s[j]-1):
                cnt += 1
        #print('cnt:', cnt)
        if cnt % 2 != P[i]:
            ok = False
    if ok:
        ans += 1
print(ans)