#bit全探索
import copy
from email.mime import nonmultipart

N,K = map(int, input().split())
buil = list(map(int, input().split()))
ans = 10**20
for bit in range(1 << N):
    mx = buil[0] #ビルの左からみた最大の高さを保持
    group = [0]
    if bit & 1: #0番目のビルは必ず見える
        for i in range(1, N):
            if bit & (1 << i):
                group.append(i)
            if len(group) == K:
                break
        if len(group) == K:
            cost = 0
            for i in range(1, N):
                if i in group: #見えるべきたてもの
                    if buil[i] <= mx:
                        mx += 1
                        cost += mx - buil[i]
                    else:
                        mx = buil[i]
                else:
                    #見えなくていいたてものなら、高さの最大の更新だけしとく
                    mx = max(mx, buil[i])
            ans = min(ans, cost)

print(ans)
