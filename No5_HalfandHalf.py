# ABピザを0～2X or 2Y枚買ったときに、足りない分を別途買ったときの合計を全探索？
 
A, B, C, X, Y = map(int, input().split())
 
ans = 5000 * 10**5 * 2
 
Z = max(X, Y)
for i in range(0, Z+1):
    P_sum = i*C*2 + max(0, X-i)*A + max(0, Y-i)*B
    ans = min(ans, P_sum)
    
print(ans)