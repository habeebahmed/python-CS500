# Write a menu-driven program that allows a user to enter a list of scores and then choose between finding the
# smallest, largest, sum, average or mode. The mode is the score that occurs the most often. It can be
# determined as a by-product of building the frequency array. After building the frequency array, use it to
# determine which score occurred the most.
# Use a if-elif statement to determine what action to take. Provide an error message if a valid choice is entered.
# Run the program five times, once with each option and once with an invalid option.
# Note: You cannot use Python built-in functions for this question. For example, collections.Counter, count(),
# sum() etc cannot be used.

def show_menu():
    print("1. Find the largest score\n2. Find the smallest score\n3. Find the sum\n4. Find the average score\n5. Find the mode of scores\n6. Exit\n")

def get_data():
    score_list_str = input("Enter a list of scores (from 0 to 10), use space as a separator: ")
    score_list = list(map(int,score_list_str.split(" ")))
    return score_list

def process_data(score_list):
    min = 10
    max = 0
    sum = 0
    average = 0.0
    mode = 0
    mode_map = {}
    mode_max = 0
    for item in score_list:
        sum += item
        if item < min:
            min = item
        if item > max:
            max = item
        if item in mode_map:
            mode_map[item] += 1
        else:
            mode_map[item] = 1

    average = sum / len(score_list)
    print(mode_map)
    for key, value in mode_map.items():
        if mode_max < value:
            mode_max = value
    mode = [k for k, v in mode_map.items() if v == mode_max ]
    return max, min, sum, average, mode

def main():
    score_list = get_data()
    processed_data = process_data(score_list)
    print(processed_data)
    while True:
        show_menu()
        choice = int(input("Please enter your choice: "))
        if (choice == 1):
            print("Largest score is: ", processed_data[0])
        elif (choice == 2):
            print("Smallest score is: ", processed_data[1])
        elif (choice == 3):
            print("Sum is: ", processed_data[2])
        elif (choice == 4):
            print("Average is: ", processed_data[3])
        elif (choice == 5):
            print("Mode is: ", processed_data[4])
        else:
            break

if __name__ == "__main__":
    main()

