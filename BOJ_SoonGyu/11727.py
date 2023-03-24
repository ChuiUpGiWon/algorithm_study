import sys
input=sys.stdin.readline

N = int(input())
graph = [0 for i in range(1001)]

graph[1] = 1
graph[2] = 3

for i in range(3,1001):
    graph[i] = (graph[i-1] + graph[i-2]*2)%10007

print(graph[N])
