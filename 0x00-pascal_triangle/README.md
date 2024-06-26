# Pascal's Triangle Generator

This Python project generates Pascal's Triangle up to a specified number of rows.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)

## Introduction

Pascal's Triangle is a triangular array of binomial coefficients. This project includes a Python function to generate Pascal's Triangle up to a given number of rows.

## Installation

To run this project, you need to have Python installed on your machine. You can download Python from the [official website](https://www.python.org/).

## Usage

Clone this repository to your local machine and navigate to the project directory.

```bash
git clone https://github.com/brikhotso/alx-interview.git
cd 0x00-pascal_triangle
```

Create a Python script (e.g., `main.py`) and import the `pascal_triangle` function.

```python
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

n = 5  # specify the number of rows
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
```

Run the script to generate Pascal's Triangle with the specified number of rows.

```bash
python main.py
```

## Example

Here is an example of how to use the `pascal_triangle` function to generate Pascal's Triangle with 5 rows.

```python
def pascal_triangle(n):
    """
    Generate Pascal's Triangle with n rows.
    
    Parameters:
    n (int): Number of rows in Pascal's Triangle.
    
    Returns:
    List[List[int]]: A list of lists representing Pascal's Triangle.
    """
    triangle = [[1]]  # initialize with the first row
    i = 1  # row number 1

    while i < n:
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
        i += 1

    return triangle

# Example usage
n = 5
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
```

Output:
```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
