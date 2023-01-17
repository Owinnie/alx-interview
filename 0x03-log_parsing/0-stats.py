#!/usr/bin/python3
""" Log Parsing """


import sys

s_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        ls_line = line.split(" ")
        if len(ls_line) > 4:
            code = ls_line[-2]
            file_size = int(ls_line[-1])
            if code in s_codes.keys():
                s_codes[code] += 1
            total_size += file_size
            count += 1

        if count == 10:
            count -= count  # reset count
            print('File size: {}'.format(total_size))
            for k, v in sorted(s_codes.items()):
                if v != 0:
                    print('{}: {}'.format(k, v))

except Exception as e:
    pass

finally:
    print('File size: {}'.format(total_size))
    for k, v in sorted(s_codes.items()):
        if v != 0:
            print('{}: {}'.format(k, v))
