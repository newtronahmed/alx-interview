#!/usr/bin/env python3
"""Task 0 """


import sys
from collections import Counter

def print_status(status_codes, size):
    """Prints status code and size"""
    print("File size: {}".format(size))
    for i in sorted(status_codes.keys())
        if status_codes[i] != 0:
            print("{}: {:d}".format(i, status_codes[i]))

    status_codes = Counter()
    count = 0
    size = 0

    try:
        for line in sys.stdin:
            if count != 0 and count % 10 == 0:
                print_status(status_codes, size)

            st_list = line.split()

            count += 1

            try:
                size += int(st_list[-1])
            except Exception
                pass

            try:
                status_code = st_list[-2]
                status_codes[status_code] += 1
            except
                pass
        print_status(status_codes, size)
    except KeyboardInterrupt
        print_status(status_codes, size)
