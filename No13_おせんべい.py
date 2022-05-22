#bit全探索
#Rは上限が10と小さいので全探索可能
import copy

R,C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

#Rに対してbit全探索
ans = 0
for bit in range(1 << R):
    A_copy = copy.deepcopy(A)
    for i in range(R):
        if bit & (1 << i):
            for j in range(C):
                A_copy[i][j] = A_copy[i][j] ^ 1 #xorでひっくり返す

    #列をひっくり返す(最終的に裏側の数が多くなればいい)
    #各列に対して、1が多いならひっくり返す、0が多いならそのまま
    mochi = 0
    for i in range(C):
        cout = 0
        for j in range(R):
            if A_copy[j][i] == 1:
                cout += 1 #現在表側の数
        if cout > R-cout:
            mochi += cout #裏返して、販売できるもちとなった数
        else:
            mochi += R-cout #裏返さずに、すでに裏のもちの数
    
    ans = max(ans, mochi)

print(ans)