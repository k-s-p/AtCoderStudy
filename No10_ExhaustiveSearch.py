#bit全探索で解く
n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

for j in range(q):
    ans = False
    for bit in range(1 << n): #1をnビット左シフト(組み合わせの全通りとなる)
        a = 0
        #print(bin(bit))
        for i in range(n):
            if bit & (1 << i): #1をiビット左シフトとbitの1が一致するA[i]が選んだもの
                a += A[i]
        if a == M[j]:
                ans = True
                break
    if ans:
        print('yes')
    else:
        print('no')