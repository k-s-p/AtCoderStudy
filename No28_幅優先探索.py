from collections import deque


def main():
    n = int(input())

    #隣接リスト作成
    G = [[]]
    for i in range(n):
        input_data = list(map(int, input().split()))
        G.append(input_data[2:])
    
    visited = [False] * (n+1)
    visited[1] = True
    Q = deque()
    Q.append(1)
    ans = [-1] * (n+1)
    ans[1] = 0
    while len(Q) > 0:
        pos = Q.popleft()
        for i in G[pos]:
            if visited[i] == False:
                Q.append(i)
                ans[i] = ans[pos] + 1
                visited[i] = True
                
                
    for i in range(1, n+1):
        print(i, ans[i])

if __name__ == '__main__':
    main()