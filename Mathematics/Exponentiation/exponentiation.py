t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print(pow(a,b,10**9+7))
