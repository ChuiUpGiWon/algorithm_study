#유클리드 호제법 사용
def gcd(a,b): #최대공약수, 최대공약수 식:x, y = y, x % y
    if a%b==0:
        return b
    return gcd(b,a%b)

def lcm(a,b): #최소공배수     
    return (a*b) // gcd(a,b) #a,b를 최대공약수로 나눈 몫이 최소공배수

n=int(input())

for _ in range(n):
    a, b= map(int, input().split())
    print(lcm(a,b))

