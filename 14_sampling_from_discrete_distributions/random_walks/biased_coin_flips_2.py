import random

p = 0.8
n = 1000
numberOfSuccesses = 0
for i in range(n):
    t = random.uniform(0, 1)
    if t < p:
        numberOfSuccesses += 1
print(numberOfSuccesses)
