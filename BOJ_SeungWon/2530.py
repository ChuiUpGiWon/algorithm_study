h,m,s=map(int,input().split())
t=int(input())

s+=t%60 //초계산
t=t//60
if s>=60:
    m+=1
    s-=60

m+=t%60 //분계산
t=t//60
if m>=60:
    h+=1
    m-=60

h+=t%24 //시계
if h>=24:
    h-=24

print(h,m,s)
