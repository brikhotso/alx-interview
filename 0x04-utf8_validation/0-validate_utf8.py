#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    num_bytes = 0

    for num in data:
        # If this is the first byte of a character
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7):
                continue
            else:
                return False
        else:
            # For continuation bytes, check the most significant bits are 10
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If we've finished processing all bytes, num_bytes should be 0
    return num_bytes == 0
