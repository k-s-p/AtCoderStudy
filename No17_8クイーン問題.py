#順列全探索でとける？
#縦、横にクイーンは必ず一つ存在する
import itertools

N = 8

#斜めを判定するための関数を定義
def QCheck(queens):
    for i in range(N):
        x,y = i, queens[i]
        sm = 0
        while 0 <= x < N:
            if queens[x] == y:
                sm += 1
            x += 1
            y += 1
        if sm > 1:
            return False
        x,y = i, queens[i]
        sm = 0
        while 0 <= x < N:
            if queens[x] == y:
                sm += 1
            x -= 1
            y -= 1
        if sm > 1:
            return False
        x,y = i, queens[i]
        sm = 0
        while 0 <= x < N:
            if queens[x] == y:
                sm += 1
            x -= 1
            y += 1
        if sm > 1:
            return False
        x,y = i, queens[i]
        sm = 0
        while 0 <= x < N:
            if queens[x] == y:
                sm += 1
            x += 1
            y -= 1
        if sm > 1:
            return False
    return True

#入力
k = int(input())
RC = []
for i in range(k):
    r,c = map(int, input().split())
    RC.append((r,c))

#クイーンを置く組み合わせを列挙
#(7, 6, 5, 4, 3, 2, 1, 0)
#左から、1行目8列,2行目7列....8行目１列に対応
for group in itertools.permutations(range(N)):
    #入力の箇所にクイーンがあるか判定
    ok = True
    for i in range(k):
        if group[RC[i][0]] != RC[i][1]:
            ok = False
            break
    if ok == False:
        continue

    if QCheck(group):
        for i in group:
            s = ['.']*N
            s[i] = 'Q'
            print(''.join(s))
