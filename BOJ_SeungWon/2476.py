#[BOJ] 2476번 주사위 게임 / bronze 3

n=int(input())
money=0
for i in range(n):
    x,y,z=map(int,input().split())

    if x==y==z:
        money=max(money,10000+x*1000)
    elif x==y or x==z:
        money=max(money,1000+x*100)
    elif y==z:
        money=max(money,1000+y*100)
    else:
        money=max(money,max(x,y,z)*100)

print(money)
