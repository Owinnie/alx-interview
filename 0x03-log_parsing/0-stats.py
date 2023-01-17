#!/usr/bin/python3
""" Log Parsing """


import sys

s_codes = dict()
total_size = 0
count = 0

try:
    for line in sys.stdin:
        ls_lines = line.split(" ")  # split line at spaces
        if len(ls_lines) > 4:
            file_size = int(ls_lines[-1])
            code = ls_lines[-2]
            if code in s_codes.keys():
                s_codes[code] += 1
            else:
                s_codes[code] = 0
            total_size += file_size
            count += 1

        if count == 10:
            count -= count  # reset count
            print(f"File size: {total_size}")
            for k, v in sorted(s_codes.items()):
                if v != 0:
                    print(f"{k}: {v}")

except Exception as e:
    pass

finally:
    print(f"File size: {total_size}")
    for k, v in sorted(s_codes.items()):
        if v != 0:
            print(f"{k}: {v}")
