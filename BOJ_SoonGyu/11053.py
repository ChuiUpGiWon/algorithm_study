import sys
input = sys.stdin.readline
#11053

N = int(input())
graph = list(map(int,input().split()))
dp = [0] * N

for i in range(N):
    for j in range(i):
        if graph[i] > graph[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))