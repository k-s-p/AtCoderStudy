#順列全探索
#pythonのitertoolsは辞書順に順列を出力する
import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

cout = 0
p,q = 0,0
for group in itertools.permutations(range(1,N+1)):
    cout += 1
    if group == P:
        p = cout
    if group == Q:
        q = cout
    if p < 0 and q < 0:
        break

print(abs(p-q))