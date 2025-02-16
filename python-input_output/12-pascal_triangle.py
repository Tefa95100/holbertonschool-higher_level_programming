#!/usr/bin/python3
"""
Contains a function for return a pascal triangle
"""


def pascal_triangle(n):
    """
    Function for return a pascal triangle

    Args:
        n (int): number of line for triangle

    Returns:
        matrix: Return a representation of pascal triangle
    """
    # Initialize
    triangle = []
    triangle_row = []
    previous_row = []

    # Case or n is less of 1
    if n <= 0:
        return triangle

    for index in range(n):
        # Handle the first line
        if index == 0:
            triangle_row.append(1)

        else:
            for index_row in range(index + 1):
                # Add 1 in line if the start or end
                if index_row == 0 or index_row == index:
                    triangle_row.append(1)
                # Add 2 element of previous line and append in this line
                else:
                    triangle_row.append(previous_row[index_row - 1] +
                                        previous_row[index_row])

        # Add the line in triangle and reinitialize the line after save
        triangle.append(triangle_row)
        previous_row = triangle_row
        triangle_row = []

    return triangle
