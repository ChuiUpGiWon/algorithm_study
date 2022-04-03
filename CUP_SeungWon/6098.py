miro = [list(map(int, input().split())) for _ in range(10)]#2차원리스트 선언과 동시에 입력받기
x=1
y=1

while True:
    if miro[x][y]==0: #벽없으면
        miro[x][y]=9 #9
    elif miro[x][y]==2: #간식위치 도달하면
        miro[x][y]=9 #9
        break #끝내기
    if miro[x][y+1]!=1: #오른쪽에 벽이 없으면
        miro[x][y]=9 #9
        y+=1 #오른쪽으로 이동
    else: #오른쪽에 벽이 있으면
        if miro[x+1][y]!=1: #아래로, 아래에 벽이 없으면
            miro[x][y]=9 #9
            x+=1 #아래로 이동
        else: #아래에 벽이 있으면
            miro[x][y]=9 #9
            break #끝내기
   
for i in range(10):
    for j in range(10):
        print(miro[i][j], end=' ')
    print()
