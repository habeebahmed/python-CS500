# Write a function that copies a one-dimensional list of n elements into a two-dimensional list of k rows and j columns. The rows and columns must be a valid factor of the number of elements in the one-dimensional array; that is, 
# k * j = n. 
# First, the function should make sure the number of items in the 1-D list equals the number of rows times the number of columns in the 2-D list. It should print an error message, do nothing, and return if they are not the same. 
# def copy1Dto2DList(oneDList, twoDList): 
# Write a program that makes use of this function

def copy1Dto2DList(oneDlist, twoDlist):
    n = len(oneDlist)
    k = len(twoDlist)
    j = len(twoDlist[0])

    if n != k * j:
        print("Error! They are not compatible")
        return

    i = 0
    for r in range(k):
        for c in range(j):
            twoDlist[r][c] = oneDlist[i]
            i += 1

def main():
    oneDlist = [2, 4, 6, 8, 5, 7]
    twoDlist = [0] * 2
    twoDlist[0] = [0] * 3
    twoDlist[1] = [0] * 3

    copy1Dto2DList(oneDlist, twoDlist)
    print(twoDlist)


if __name__ == '__main__':
    main()

