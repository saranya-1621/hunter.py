m = int(input())
n = input().split()
flag = 0
for i in n:
  if n.count(i) > 1:
    print(int(i))
    flag = 1
    break
    
if flag == 0:
  print("unique")
