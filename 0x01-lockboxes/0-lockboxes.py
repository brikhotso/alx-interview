#!/usr/bin/python3
""" lockboxes """


def canUnlockAll(boxes):
    """
    This function determines if all the boxes can be opened.

    Parameters:
    boxes (list of lists): sublist contains keys to the other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set()

    def dfs(i):
        """
        Helper function to perform depth-first search.

        Parameters:
        i (int): Index of the current box.
        """
        visited.add(i)
        for key in boxes[i]:
            if key not in visited and key < n:
                dfs(key)

    dfs(0)

    return len(visited) == n
