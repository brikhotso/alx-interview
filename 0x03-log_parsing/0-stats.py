#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics. """
import sys


def print_status(status_codes, total_size):
    """Print the status codes and file size."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        if line_count and line_count % 10 == 0:
            print_status(status_codes, total_size)

        parts = line.split()
        line_count += 1

        try:
            total_size += int(parts[-1])
        except ValueError:
            pass

        try:
            if parts[-2] in status_codes:
                status_codes[parts[-2]] += 1
        except IndexError:
            pass

    print_status(status_codes, total_size)

except KeyboardInterrupt:
    print_status(status_codes, total_size)
    raise
