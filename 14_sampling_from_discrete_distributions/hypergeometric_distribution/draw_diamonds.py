import random

N = 52  # cards in total
M = 13  # diamonds
n = 10  # cards drawn

drawDiamonds = 0

for i in range(n):
    t = random.uniform(0, 1)
    if t < M / N:
        drawDiamonds += 1
        M -= 1
    N -= 1
print(drawDiamonds)
