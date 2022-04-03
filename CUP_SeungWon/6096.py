board=[[0 for j in range(19)] for i in range(19)] #19*19 2차원리스트생성

for i in range(19): #입력값 리스트에 입력
    board[i]=list(map(int, input().split()))

n=int(input()) #십자뒤집기 횟수 입력받기

for i in range(n):  #십자뒤집기 횟수만큼
    x,y=map(int,input().split()) #십자뒤집기 좌표 입력받기

    for j in range(19):
        if board[x-1][j]==0: #x축 고정시키고 y값 바꾸면서 0->1, 1->0
            board[x-1][j]=1
        else:
            board[x-1][j]=0
        if board[j][y-1]==0: #y축 고정시키고 x값 바꾸면서 0->1, 1->0
            board[j][y-1]=1
        else:
            board[j][y-1]=0

for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    print()
