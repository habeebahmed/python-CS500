# Assume that a video store has two employees, they've got different hours of work last week. They get paid $14.50 for the first 40 hours; They get time-and-a half pay (1.5 times the regular pay rate) for the first five hours over 40; and they get double-time pay for all hours over 45. Assuming a 28-percent tax rate, write a program that prompts the user to enter their hours of work, print their gross pay, taxes and net pay on the screen. Label each amount with appropriate titles and add appropriate comments in the program.

# CODE LOGIC
# case 1: <= 40
# 14.50 * hours

# case 2: <= 45
# 14.50* 40 + 1.5(14.50)(hours - 40)

# case 3: > 45
# 14.50* 40 + 1.5(14.50)(5) + 2(14.50)(hours-45)

print("Calculating the gross, tax and net pay for two employees")

# Hard coding the payRate and numEmployees
pay_rate = 14.5
num_employees = 2

for i in range(num_employees):
    hours = int(input("Please enter the number of work hours: "))
    gross_pay = 0
    # case 1: <= 40
    # 14.50 * hours
    if hours <= 40:
        gross_pay = hours * pay_rate
    # case 2: <= 45
    # 14.50* 40 + 1.5(14.50)(hours - 40)
    elif hours <= 45:
        gross_pay = 40 * pay_rate + (1.5 * pay_rate * (hours - 40))
    # case 3: > 45
    # 14.50* 40 + 1.5(14.50)(5) + 2(14.50)(hours-45)
    else:
        gross_pay = 40 * pay_rate + (1.5 * pay_rate * 5) + (2 * pay_rate * (hours - 45))
    # Tax is 28% of gross pay
    tax = gross_pay * 0.28

    # Display Gross, Tax and Net pay
    print("The gross pay is ${}".format(round(gross_pay,2)))
    print("The tax is ${}".format(round(tax,2)))
    print("The net pay is ${}".format(round(gross_pay - tax,2)))

    