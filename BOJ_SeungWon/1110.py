n=input()
num=n
count=0
while 1:
    if len(num)==1:
        num="0"+num
        n=num
    right=str(int(num[0])+int(num[1]))
    num=num[-1]+right[-1]
    count+=1
    if num==n:
        break
print(count)


