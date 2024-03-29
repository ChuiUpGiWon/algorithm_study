import sys
input = sys.stdin.readline
from collections import deque
#11660

N,M = map(int,input().split())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    row = list(map(int,input().split()))
    graph.append(row)

dp = [[0]* (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i][j-1]+dp[i-1][j] - dp[i-1][j-1] + graph[i-1][j-1]

for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)
