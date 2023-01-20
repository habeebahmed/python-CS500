# Use lambda function and list comprehension only takes a list of strings and returns a new list of strings with a vowel as the last character (a, e,i, o, and u).

# Example,

# input: [“car”, “ABBA”, “def”, “love”, “Orange”, “anti”]

# Return: [“ABBA”, “love”, “Orange”, “anti”]

def main():
    n: int = int(input("Enter the number of strings: "))
    arr: list[str] = []
    print(f"Enter {n} strings one after the other using enter/return key as separator")
    for i in range(n):
        arr.append(str(input()))

    # list comprehension and lambda

    arr_res: list[str] = list(filter(lambda x: x[-1].lower() in ['a', 'e', 'i', 'o', 'u'], arr))
    arr_res = [ word for word in arr if (lambda x: x[-1].lower() in "aeiou")(word) ]

    print(arr_res)

main()