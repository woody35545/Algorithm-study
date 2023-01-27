def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a * b / gcd(a, b)

def check(a:int, b:int)->bool:
    lcm_ab = lcm(a,b)
    mult_ab = a*b
    if lcm_ab == mult_ab:
        return True
    return False


N = int(input())

for i in range(N):
    a,b = map(int,input().split(" "))
    if check(a,b):
        print("Perfect")
    else:
        print("Not even close")
