t = int(input())
print(t, end=" ")
while(t != 1):
    if t % 2 == 0:
        t = t // 2
    else:
        t = 3 * t + 1
    print(t,end = " ")
