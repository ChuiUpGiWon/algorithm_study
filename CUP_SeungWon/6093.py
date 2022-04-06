num=int(input())
numlist=input().split()

stdlist=list()
for i in range(num-1,-1,-1):
    stdlist.append(numlist[i])
for i in range(0,num):
    print(stdlist[i], end=' ')
    
