d = int(input())
n = int(input())
m = int(input())
d_i = [int(input()) for _ in range(n-1)]
k_i = [int(input()) for _ in range(m)]

#本店を位置0,dの店舗として、店舗をソート
#その後、k_iの宅配先のどこに一番近いかを二分探索で求める
d_i.append(0)
d_i.append(d)
d_i.sort()
# print(d_i)

#二分探索
ans = 0
for k in k_i:
    left = -1
    right = len(d_i)
    while abs(right - left) > 1:
        mid = (right + left) // 2
        if d_i[mid] >= k:
            right = mid
        else:
            left = mid
    a = abs(d_i[left]-k)
    b = abs(d_i[right]-k)
    ans += min(a,b)

print(ans)