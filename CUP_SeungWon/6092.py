num=int(input())
numlist=input().split()

stdlist=list()
for i in range(24):
    stdlist.append(0)
for i in range(num):
    stdlist[int(numlist[i])]+=1
for i in range(1,len(stdlist)):
    print(stdlist[i], end=' ')
