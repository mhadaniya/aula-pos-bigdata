#!/usr/bin/env python

import csv
import sys

def mapper():
    for row in sys.stdin:
        #row = row.strip()
        data = next(csv.reader([row], delimiter='\t'))

        sub, _, body, _, _, _, _, _ = data

        #TODO

if __name__ == "__main__":
    mapper()