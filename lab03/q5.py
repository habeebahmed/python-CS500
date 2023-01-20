# Create a program that displays a 4 option menu. The options to be included are:
# e - Enter a new employee's information
# a - Display all employees information
# d - Display an employee's information
# q - Quit
# ● Option e:
# ○ Prompt a user to provide the name, ID, department number, and age of an employee. Store the
# information as a list of employees. Each employee is represented by a list of items that include
# their name, ID, department number, and age.

# ● Option a:
# ○ Display information entered for all employees.
# ● Option d:
# ○ If option d is selected, prompt the user for the employee's name. Search the list. If found,
# display the employee. If not found, allow the user to enter the new employee if they choose.

import sys


def print_menu_options():
    print('''
    e - Enter a new employee's information \n
    a - Display all employees information \n
    d - Display an employee's information \n
    q - Quit
    ''')

def new_employee(emp_list):
    new_emp = {'name': '', 'id': '', 'dept_num': '', 'age': 0}
    new_emp['name'] = input("Please enter employee name: ")
    new_emp['id'] = input("Please enter employee ID: ")
    new_emp['dept_num'] = input("Please enter department number: ")
    new_emp['age'] = int(input("Please enter age of employee: "))
    emp_list.append(new_emp)
    pass         

def all_employees(emp_list):
    if not emp_list:
        print("No employees added")
    else:
        print("retrieving employee information")
        print('%-10s%-5s%-18s%-5s'%('Name', 'ID', 'Department Number', 'Age'))
        for emp in emp_list:
            print('%-10s%-5s%-18s%-5i' % (emp['name'], emp['id'], emp['dept_num'], emp['age']))

def one_employee(emp_list):
    search_name = input("Enter employee name to search for: ")
    match = [x for x in emp_list if x['name'] == search_name]
    if bool(match):
        result = match[0]
        print("Record found!!!!!")
        print('%-10s%-5s%-18s%-5s'%('Name', 'ID', 'Department Number', 'Age'))
        print('%-10s%-5s%-18s%-5i' % (result['name'], result['id'], result['dept_num'], result['age']))
    else:
        print("No matching record for name ", search_name)
        conf = input("Enter new record for " + search_name + " (y/n)")
        if conf == 'y':
            new_employee(emp_list)

def quit(emp):
    print("Good bye")
    sys.exit(0)


def main():
    print("Employees Information \n")
    emp_list = []
    options = { 'e': new_employee, 'a': all_employees, 'd': one_employee, 'q': quit }
    while True:
        print_menu_options()
        choice  = input('Please select any option: ')
        options[choice](emp_list)

        


if __name__=="__main__":
    main()