#前からACGT以外の文字が出るまでをカウント、でたら一度切って次のカウントを始める
 
S = input()
 
count = 0
ans = 0
for i in range(len(S)):
    if S[i] != 'A' and S[i] != 'C' and S[i] != 'G' and S[i] != 'T':
        count = 0
        continue
    else:
        count += 1
        ans = max(ans, count)
print(ans)