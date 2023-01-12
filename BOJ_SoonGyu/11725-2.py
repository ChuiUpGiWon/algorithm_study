import sys
from collections import deque
#11725
input = sys.stdin.readline

N = int(input())
graph =[[] for i in range(N+1)]
result = []

for i in range(N-1):
    num1, num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

BFS = [0] * (N+1)

def bfs(v):
    q = deque()
    q.append(v)
    BFS[v] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not BFS[i]:
                BFS[i] = v
                q.append(i)

bfs(1)

for i in range(2,N+1):
    print(BFS[i])
