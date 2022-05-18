N = int(input())
 
ans = 0
for i in range(1, N+1):
    num = 0
    if i%2 == 1:
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                num += 1
        if num == 4:
            ans += 1
            
print(ans)