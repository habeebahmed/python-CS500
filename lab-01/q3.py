# Write a Python program that gets an integer (n) from the user and computes the value of n+2nn+ 3nnn
# e.g:
# if n is 123
# then
# the value should be obtained by 123 + 2123123 + 3123123123 = 3125246369

print("Calculating the formula n+2nn+ 3nnn")
n = input("Enter n's value: ")
# String concatenation and type casting to integer
computed_value = int(n) + int("2"+n+n) + int("3"+n+n+n)
print("Computed value: ", computed_value)