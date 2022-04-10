h,m=map(int,input().split())
t=int(input())

h+=t//60 #나누고 정수부분만
m+=t%60 #나누고 나머지 
if m>=60:
    h+=1
    m-=60
if h>=24:
    h-=24
    
print(h, m)
