# Use the list comprehension to take a list of integers and return a new list with the sums of two adjacent numbers.  

 

# Ex1:

# Input: [10, 20, 30, 40, 50, 60]

# Return: [30, 70, 110]

 

# Ex2:

# Input: [2, 4, 6, 8, 10]

# Output: [6, 14, 10]


def main():
    n = int(input("Enter the number of digits: "))
    arr: list[int] = []
    print(f"Enter {n} number one after the other using enter/return key as separator")
    for i in range(n):
        arr.append(int(input()))

    # sum of two adjacents
    arr_new: list[int] = [arr[i] + arr[i+1] if i+1 < n else arr[i] for i in range(n) if i%2 == 0]
    print(arr_new)

main()