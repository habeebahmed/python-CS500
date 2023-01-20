# The trace of a square matrix (i.e. a two-dimensional list with the same number of rows as columns) is the sum
# of its diagonal elements. For example, the trace of the matrix
# 4 6 7 3 2
# 7 5 8 5 6
# 8 2 1 2 1
# 3 3 6 4 7
# 6 4 9 5 3
# is 4 + 5 + 1 + 4 + 3 = 17.
# Implement the following trace() function:
# def trace(matrix);
# Write a program that makes use of this function

def trace(matrix):
    '''
    Get trace of matrix
    '''
    print("Display the array In Matrix Form: ")
    trace_of_matrix = 0
    n = len(matrix)
    # Show inpput array in matrix form
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

    # Iterate to calculate the left diagnoal sum
    for x in range(0, n):
        for y in range(0, n):
            if x + y == n-1:
                trace_of_matrix = trace_of_matrix + matrix[x][y]
    return trace_of_matrix    

def main():
    # To find Trace of the given Matrix
    print("Find trace of a given matrix")
    matrix = []
    n=int(input("Enter the size of the matrix: "))

    # get matrix input
    print("Enter the elements: ")
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(int(input()))
        matrix.append(row)
    
    trace_of_matrix = trace(matrix)
    print( "Sum of trace of matrix: ",trace_of_matrix)


if __name__ == "__main__":
    main()