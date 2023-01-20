# A school cafeteria is giving an electronic survey to its students to improve their lunch menu. Create a program
# that uses a list to store votes for the survey. The program should display four food items in the display. Then it
# prompts students to enter whether they like or dislike a particular food. Display a report that’s updated as each
# new set of responses is entered. Use a 2-D Integer array named votes, with four rows and two columns to
# summarize the results. Each row corresponds to a food item. The columns store the number of “like” and
# “dislike” votes, respectively.

#       Like Dislike
# Pizza 2 0
# Hot Dog 1 1
# Ham 0 2
# Cheese 1 1


def generate_report(food_rating, food_items):
    print("Report of likes and dislikes by students on different food items\n")
    print("\t\tLike\tDislike")
    for key, value in food_items.items():
        print("{}\t\t{}\t{}".format(value, food_rating[key-1][0], food_rating[key-1][1]))

def main():
    food_rating = [[0,0], [0,0], [0,0], [0,0]]
    food_items = {1: 'Pizza', 2: 'Hot Dog', 3: 'Ham', 4: 'Cheese'}
    while True:
        for key, value in food_items.items():
            answer = input("Do you like " + value + "please enter (y/n)")
            if answer == "y":
                food_rating[key-1][0] +=  1
            else:
                food_rating[key-1][1] +=  1
        
        conf = input("Do you have any another student, (y/n): ")
        if conf == 'n':
            break
    generate_report(food_rating, food_items)

if __name__=="__main__":
    main()