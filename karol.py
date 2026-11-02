tests = int(input())
for _ in range(tests):
    wage, goal = [int(x) for x in input().split()]
    bank = wage
    count = 1
    while bank < goal:
        count +=1
        wage *= 2
        bank += wage
    print(count)
