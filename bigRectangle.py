num = int(input())
heights = []
for _ in range(num):
    heights.append(int(input()))

currA = 0
maxA = 0

for i in range(num):
    left = i
    while left > 0 and heights[left - 1] >= heights[i]:
        left-= 1

    right = i
    while right < num - 1 and heights[right + 1] >= heights[i]:
        right += 1

    width = right - left + 1

    currA = width*heights[i]
    maxA = max(currA, maxA)

print(maxA)
