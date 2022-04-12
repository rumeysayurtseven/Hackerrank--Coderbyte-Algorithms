"start"
io = input().split()
m = int(io[0])
n = int(io[1])
A = set(map(int, input().split()))
B = set(map(int, input().split()))
arr = list()
arr = list(map(int,input().strip().split()))
inithapp=0

for i in arr:
    if i in A:
        inithapp += 1
    elif i in B:
        inithapp -= 1
    else:
        inithapp
print(inithapp);
  
"end"
