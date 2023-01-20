# Read a sequence of words from the keyboard. Use Exit as a word that terminates the input. Print the words in
# the order they were entered. Modify the program to sort the words before printing them. Don’t print a word
# twice.

def print_sequence_of_words(words):
    # sort the list alphabetically
    words.sort()
    for word in words:
        print(word)

def main():
    words = []
    # Infinite loop terminate on 'Exit' keyword
    while (True):
        word = input("Please enter a word: ")
        if word == 'Exit':
            break
        if word in words:
            continue
        words.append(word)
    print_sequence_of_words(words)

if __name__ == "__main__":
    main()