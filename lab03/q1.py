# (Decimal to hex) Write a program that prompts the user to enter an integer between 0 and 15 and displays its
# corresponding hex number. Here are some sample runs:
# Enter a decimal value (0 to 15): 11
# The hex value is B
# Enter a decimal value (0 to 15): 5
# The hex value is 5
# For converting decimal to hex, you should NOT use Python's built-in methods.

def dec_to_hex(dec):
    hex_dic = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }
    if (dec >= 10 and dec <= 15):
        return hex_dic[dec]
    elif (dec >= 0 and dec <= 9):
        return str(dec)
    else:
        raise ValueError("Please enter a valid number")

def main():
    try:
        print("Convert 0 - 15 decimal numbers to hexadecimal")
        dec = int(input("Enter decimal number between 0 and 15: "))
        hex = dec_to_hex(dec)
        print("The hex value is ", hex)
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()