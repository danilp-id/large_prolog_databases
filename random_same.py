#!/bin/env python3

# Use the same statistics for 3 variants (ints, atoms, strings)

import random

nvocab = 100

vocab = []
for i in range(nvocab):
    s = ""
    for l in range(random.randint(10, 100)):
        s += chr(random.randint(ord('a'), ord('z')))
    vocab.append(s)

def randint():
    return random.randint(0, nvocab-1)

# def randstr():
#     return f'"{random.choice(vocab)}"'

ints = open("random_ints.pl", "w")
strs = open("random_strs.pl", "w")
num_strs = open("random_num_strs.pl", "w")
atms = open("random_atoms.pl", "w")

for i in range(100000):
    a = randint()
    b = randint()
    c = randint()
    d = randint()

    ints.write(f"a({a}, {b}, {c}, {d}).\n")
    num_strs.write(f'a("{a}", "{b}", "{c}", "{d}").\n')
    strs.write(f'a("{vocab[a]}", "{vocab[b]}", "{vocab[c]}", "{vocab[d]}").\n')
    atms.write(f"a({vocab[a]},{vocab[b]},{vocab[c]},{vocab[d]}).\n")