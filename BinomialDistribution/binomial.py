# -*- coding: utf-8 -*-
"""
    Created on 04.09.2017 10:27
    @author: Kristoffer-Andre Kalliainen
"""
import random

probability = 0.8  # probability of success
number = 14  # number of trials


def get_binomial(n, p):
    def run():
        positives = 0
        for i in range(n):
            t = random.uniform(0, 1)
            if t < p:
                positives += 1
        return positives

    return run()


variance = 0
p = 1 / 6
numberOfTrials = 100
n = 15
for i in range(numberOfTrials):
    numberOfSuccesses = 0
    for j in range(n):
        t = random.uniform(0, 1)
        if t < p:
            numberOfSuccesses += 1
    variance += (numberOfSuccesses - n * p) ** 2
variance /= (numberOfTrials - 1)

sixes = get_binomial(15, 1 / 6)
print(sixes)

print(variance)
