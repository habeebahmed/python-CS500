# Write a program that creates the following pattern, get the width (maximum number of asterisks) as an input.
#      *
#     **
#    ***
#   ****
#  *****
# ******
#  *****
#   ****
#    ***
#     **
#      *
# n = 6

def print_pattern(num):
    count = 0
    for i in range(2*num - 1):
        # decrease symbol number and increase space
        if i >= num:
            count -= 1
            print(" " * (i % num + 1 ) + "*" * (count))
        # increase symbol and decrease space
        else:
            count += 1
            print(" " * (num - i - 1) + "*" * (count) )

def main():
    num = int(input("Enter the width of pattern: "))
    print_pattern(num)

if __name__=="__main__":
    main()