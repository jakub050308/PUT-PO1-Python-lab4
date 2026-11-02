w1,h1 = [int(x) for x in input().split()]

m1 = []
for i in range(h1):
    r = list(int(x) for x in input().split())
    m1.append(r)


w2,h2 = [int(x) for x in input().split()]

m2 = []
for i in range(h2):
    r = list(int(x) for x in input().split())
    m2.append(r)

result = [[0] * w2 for _ in range(h1)]

for i in range(h1):

    for j in range(w2):
        for k in range(h2):
            result[i][j] += m1[i][k] * m2[k][j]


for i in range(h1):
    for j in range(w2):
        print(result[i][j], end=' ')
    print("")
