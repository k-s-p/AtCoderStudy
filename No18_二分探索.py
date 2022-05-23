n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

#S要素内を二分探索し、Tの要素があればans += 1
ans = 0
for t in T:
    left = -1
    right = n
    while abs(right - left) > 1:
        mid = (right + left) // 2
        if S[mid] >= t:
            right = mid
        else:
            left = mid
    if right == n:
        continue
    if S[right] == t:
        ans += 1

print(ans)