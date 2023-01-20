# Write a program to, given a square matrix with elements of 0 or 1, find the first square submatrix with all 1
# elements. This square submatrix should be as big as it can be, but it must include only ones and be at least 3
# in size. Your program should prompt the user to enter the number of rows in the matrix. The number of rows
# should be at least 5. The program then displays the location of the first element in the square submatrix and
# the number of the rows in the submatrix. Here is a sample run:
# Example 1:
# Enter the number of rows in the matrix: 6
# Enter the matrix row by row:
# 101011
# 111011
# 101111
# 101111
# 101111
# 111111

# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 0 1 1 1 1 1
# 1 0 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 0 1 0 1
# 1 1 1 0 1
# 1 1 1 0 1
# 1 1 1 0 0
# 1 1 1 0 0
# The first square submatrix is at (2, 2) with size 4

# Your program should implement and use the following method to find the first square submatrix with the
# minimum size 3.
# def find_first_squareblock(matrix : list[int]) -> list[int]
# The return value is a list that consists of three values. The first two values are the row and column indices for
# the first element in the submatrix, and the third value is the number of the rows in the submatrix.
from typing import List


def find_first_squareblock(matrix: List[List[int]]) -> List[int]:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    # Initialise a 2d array with zeros
    dp: List[List[int]] = [[0]*(cols) for _ in range(rows)]
    result: List[int] = [0, 0, 0]
    for i in range(rows):
        for j in range(cols):
            # skip first row and first col for calculation
            if matrix[i][j] == 1 and i != 0 and j != 0:
                # get the minimum of surrounding top, left and top-left element
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                # record the first found 3 (since as per question: find the first square submatrix with the minimum size 3.)
                if result[2] == 0 and dp[i][j] == 3:
                    result[0] = i - 2
                    result[1] = j - 2
                    result[2] = 3
            else:
                dp[i][j] = matrix[i][j]

    # look for maximum size from here
    k: int = result[0] + 3
    l: int = result[1] + 3
    while k < rows and l < cols:
        if dp[k][l] > result[2]:
            result[2] = dp[k][l]
        else:
            break

    return result


def main() -> None:
    print("Find the first square matrix with minimum size 3")
    rows: int = int(input("Enter the number of rows in the matrix (min 5): "))

    matrix: List[List[int]] = [[0]*(rows) for _ in range(rows)]
    # take input row by row each value separated by space
    print("Enter the matrix row by row:")
    for j in range(rows):
        temp: str = input()
        list_of_var_int: list[int] = list(map(int, temp.split(" ")))
        count: int = 0
        for k in list_of_var_int:
            matrix[j][count] = k
            count += 1
    max: List[int] = find_first_squareblock(matrix)
    print(max)


if __name__ == "__main__":
    main()
