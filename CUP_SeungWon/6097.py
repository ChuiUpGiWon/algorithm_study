h,w=map(int,input().split()) #세로,가로
n=int(input()) #막대의개수


#list=[[0 for j in range(w)] for i in range(h)]
list=[[0]* w for _ in range(h)] #0으로 채워진 이차배열 생성

for i in range(n):
    l,d,x,y=map(int,input().split()) #막대길이,방향,좌표(x,y)
    for j in range(l):
        if d==0:
            list[x-1][y-1+j]=1
        else:
            list[x-1+j][y-1]=1

for i in range(h):
    for j in range(w):
        print(list[i][j], end=' ')
    print()
