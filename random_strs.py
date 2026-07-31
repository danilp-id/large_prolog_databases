#!/bin/env python3

import random

nvocab = 100

vocab = []
for i in range(nvocab):
    s = ""
    for l in range(random.randint(10, 100)):
        s += chr(random.randint(ord('a'), ord('z')))
    vocab.append(s)

# def randint():
#     return random.randint(0, nvocab)

def randstr():
    return f'"{random.choice(vocab)}"'

for i in range(100000):
    print(f"a({randstr()}, {randstr()}, {randstr()}, {randstr()}).")