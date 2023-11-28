#!/usr/bin/python3
"""
A module for working with Pascal's triangle.
"""
def pascal_triangle(n):
    """
    Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    """

    triangle = []
    if type(n) is not int or n <= 0:
        return []
    for i in range(1, n+1):
        line = []
        C = 1
        for j in range(1, i+1):
            
            line.append(C)
            C = C * (i - j) // j
        triangle.append(line)
    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
