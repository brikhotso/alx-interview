#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be unlocked, else return False.

    Parameters:
    boxes (list of lists): Sublist contains keys to the other boxes.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    total_boxes = len(boxes)
    opened_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key < total_boxes and key not in opened_boxes:
                opened_boxes.add(key)
                new_keys.update(boxes[key])
        if not new_keys:
            break
        keys = new_keys

    return total_boxes == len(opened_boxes)
