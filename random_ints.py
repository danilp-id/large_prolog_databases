#!/bin/env python3

import random

nvocab = 100

def randint():
    return random.randint(0, nvocab)

for i in range(100000):
    print(f"a({randint()}, {randint()}, {randint()}, {randint()}).")