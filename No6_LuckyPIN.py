# 全探索で求める
# 3桁の000～999を作ることが可能かを探索する。
 
N = int(input())
S = input()
 
ans = 0
for i in range(1000):
    key = str('000' + str(i))[-3:]
    #print(key)
    idx = 0
    for j in range(N):
        if S[j] == key[idx]:
            idx += 1
        if idx == 3:
            ans += 1
            break
 
print(ans)