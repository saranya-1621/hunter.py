na = int(input())
la = list(map(int,input().split()))

for i in range(len(la)):
    if i % 2 == 0 and la[i] % 2 == 1:
        print(la[i],end =' ')
    if i % 2 == 1 and la[i] % 2 == 0:
        print(la[i],end =' ')
