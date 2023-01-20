# Suppose you put $10,000 into a CD with an annual percentage yield of 5.75%. After one month, the CD is worth 10000 + 10000 * 5.75 / 1200 = 10047.91 After two months, the CD is worth 10047.91 + 10047.91 * 5.75 / 1200 = 10096.06 After three months, the CD is worth 10096.06 + 10096.06 * 5.75 / 1200 = 10144.43 and so on. Write a program that prompts the user to enter an amount (e.g., 10000), the annual percentage yield (e.g., 5.75), and the number of months (e.g., 18) and displays a table as shown in the sample run. The format of the output should match the following sample.


# The CD Calculator
print("The CD Calculator")
# Enter the initial deposit amount: 10000
principal = float(input("Please enter initial deposit: "))
# Enter annual percentage yield: 5.75
annual_percentage_yield = float(input("Please enter annual percentage yield: "))
# Enter maturity period in months
maturity_period = int(input("Please enter maturity period in months: "))
# Month CD
print("Month CD")
# iterate on maturity period and calculate the CD for each month
for idx, i in enumerate(range(maturity_period)):
    principal += principal * (annual_percentage_yield / 1200)
    print("{} ${}".format(idx+1, round(principal, 2)))