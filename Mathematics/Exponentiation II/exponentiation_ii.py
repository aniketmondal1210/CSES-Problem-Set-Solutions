t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    print(pow(a,pow(b,c,10**9+6),10**9+7))
