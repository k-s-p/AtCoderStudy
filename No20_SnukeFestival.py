N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

#Bに着目して、条件を満たすAの境界、Cの境界を二分探索で求める
A.sort()
C.sort()
ans = 0
for b in B:
    #A_i < B_iを満たすA_iを探索
    ok_a = -1
    ng_a = N
    while abs(ok_a-ng_a) > 1:
        mid = (ok_a+ng_a) // 2
        if A[mid] < b:
            ok_a = mid
        else:
            ng_a = mid
    #C_i > B_iを満たすC_iを探索
    ok_c = N
    ng_c = -1
    while abs(ok_c-ng_c) > 1:
        mid = (ok_c+ng_c) // 2
        if C[mid] > b:
            ok_c = mid
        else:
            ng_c = mid
    # print(ok_a, ok_c)
    ans += (ok_a+1)*(N-ok_c)

print(ans)
    