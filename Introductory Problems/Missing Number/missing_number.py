t = int(input())
a = list(map(int, input().split()))
print(t*(t+1)//2 - sum(a))
