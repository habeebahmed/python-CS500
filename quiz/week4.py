# An matrix is called a positive Markov matrix if each element is positive and the sum of the elements in each column is 1. Write the following function to check whether a matrix is a Markov matrix.

# def is_markov_matrix(matrix)

# Write a main function that prompts the user to enter the size of matrix and then a matrix of floats and tests whether it is a Markov matrix. Here are sample runs:

# Enter the size of matrix: 3

# Enter a 3-by-3 matrix row by row:

# 0.15 0.875 0.375
# 0.55 0.005 0.225
# 0.30 0.12 0.4
# It is a Markov matrix

# 0.95   -0.875  0.375 0.77
# 0.65   0.005   0.225  0.66
# 0.30   0.22     -0.4     0.88

# 0.0     0.02     0.7       0.2

def is_markov_matrix(matrix):
    for i in range(0, len(matrix)) :
        # Find sum of current column
        sm = 0
        for j in range(0, len(matrix[i])):
            val = matrix[j][i]
            # if it is negative number return false
            if val < 0:
                return False
            sm = sm + val
  
        if (sm != 1) :
            return False
              
    return True

def main():
    # try:
        size = int(input("Enter the size of matrix: "))
        # initialise a 2d array with zeroes
        matrix = [0] * size
        for i in range(size):
            matrix[i] = [0] * size
        # print("Enter a {}-by-{} matrix row by row:".format(size, size))

        for j in range(size):
            temp = input()
            list_of_var_float = list(map(float, temp.split(" ")))
            count = 0
            for k in list_of_var_float:
                matrix[j][count] = k
                count += 1
        if is_markov_matrix(matrix):
            print("It is a Markov matrix")
        else:
            print("It is not a Markov matrix")
    # except Exception as e:
    #     print("Something went wrong, please enter the data in correct format (columns separated by a space and rows in new line)")

if __name__ == "__main__":
    main()
