# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,n개의 흰 돌이 놓인 위치를 출력하는 프로그램
# 2차원 리스트 생성 : d = [[0 for j in range(20)] for i in range(20)]

list=[[0 for j in range(20)] for i in range(20)] #2차원리스트 생성

num=int(input())
for i in range(num):
    x,y=map(int, input().split()) #좌표 받기
    list[x][y]=1 #좌표를 1로 채우기

for i in range(1,20):
    for j in range(1,20):
        print(list[i][j], end=' ')
    print()


