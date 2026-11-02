a = list((int(x) for x in input().split()))
maxSum = 0
currSum = 0
dl = len(a)

for b in range(dl):
    for e in range(b, dl):
        currSum += a[e]
        if currSum > maxSum:
            maxSum = currSum
    currSum = 0
if maxSum < 0:
    print(0)
else: print(maxSum)