#!/bin/env python3

# Script to convert any csv file into a Prolog database

import pandas as pd
from sys import argv
import re

def snake2camel(s):
    ts = s.split("_")
    f = ts[0]
    r = [x.capitalize() for x in ts[1:]]
    return "".join([f.lower()] + r)

def encode(v):
    if type(v) is str:
        # check if it's a timestamp
        ts = re.findall(r"^\s*(\d?\d):(\d\d):(\d\d)\s*$", v)
        if ts:
            (h,m,s) = ts[0]
            return str(int(s) + 60*int(m) + 60*60*int(h))

        return f'"{v}"'
    if type(v) is int or float:
        return str(v)

    raise Error(f"Unsupported type: {type(v)} for {v}")

def main():
    if len(argv) < 3:
        print(f"Usage: {argv[0]} [csv_in] [prolog_out]")
        return

    df = pd.read_csv(argv[1])

    with open(argv[2], "w") as f:
        for _, row in df.iterrows():
            d = dict(row)
            keys = list(snake2camel(x) for x in d.keys())
            pred = "_".join(keys)
            vals = ', '.join(encode(v) for v in d.values())
            f.write(f"{pred}({vals}).\n")

main()