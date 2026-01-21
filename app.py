# APP REQUIREMENTS
# 1. USER ENTERS EXPENSE
# 2. SAVE EXPENSE TO CSV FILE
# 3. SUMMARISE EXPENSE TOTALS
# 4. SHOW REMAINING BUDGET

from expense import Expense
from database import initialize_database, add_expense, get_all_expenses , get_expense_by_id
import calendar
import datetime


def main(): # this can be ran af func for other app you use to avoid that and only run it when we want we will set a condition
    print(f'🎯 Running Expense Tracker')

    expense_file_path = 'expenses.db'
    budget = 5000

    initialize_database()

    #gives app index
    option_menu = get_options()


def get_options():
    options = [
        '1. Enter expense',
        '2. View expense by id',
        '3. Update expense',
        '4. Delete expense',
        '5. View all expense',
    ]
    print('\n'.join(options))

    while True:
        option = input('Choose an option: ')

        if option == '1':
            budget = 5000
            expense = get_user_expense()
            add_expense(expense)
            expenses = get_all_expenses()
            summarize_expense(expenses, budget)
            break

        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
        
        else:
            print('Invalid option! Try again!')
            break

def get_user_expense():
    print('Geting User input ')

    expense_name = input('Enter Expense Name: ')
    expense_amount = float(input('Enter Expense Amount: '))
    print(f'You have entered {expense_name}, ₹{expense_amount}')

    expense_category = [
        '🍔 Food',
        '🏡 HOME',
        '💼 WORK',
        '🎊 FUN',
        '✨ MISC',
    ]

    while True:
        print('Select a category: ')
        for i, category_name in enumerate(expense_category):
        #                        ^ enumarate gives a 2 pull response here with the index and name like : 1. 🍔FOOD
            print(f'{i+1}. {category_name}')

        value_range = f'[1 - {len(expense_category)}]'
        # ^ this line gives a range from 1 to 5 to user to choose from

        selected_index = int(input(f'Enter a category number {value_range}: ')) - 1

        if selected_index in range (len(expense_category)):

            selected_category = expense_category[selected_index]

            new_expense = Expense(
                name=expense_name, category=selected_category, amount= expense_amount
                )

            return new_expense
        
        else:
            print('Inavlid category! Choose again!') 
        
    
#                                  ⬇️ this is a type hint, use it to not make mistakes when handling multiple values
# def save_expense_to_file(expense : Expense, expense_file_path):
#     print(f'🎯 Saving user expense: {expense} to {expense_file_path}')
#     with open(expense_file_path,'a', encoding = 'utf-8') as f: # as f will create the file if it doesnt exists
# #                                ^ this  'a' will append(add) to the file as we dont want to overwrite
#         f.write(f'{expense.name},{expense.amount},{expense.category}\n')


def summarize_expense(expenses: list[Expense], budget):
    print(f'🎯 Summarizing user Expense')
    #expenses : list[Expense] = []

    # with open(expense_file_path,'r', encoding = 'utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         stripped_line = line.strip()
    #         expense_name,expense_amount,expense_category = line.strip().split(',')

    #         line_expense = Expense( name = expense_name, amount = float(expense_amount), category = expense_category)
    #         print(line_expense)
    #         expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print('Expense by category : ')
    for key , amount in amount_by_category.items():
        print(f'  {key} : ₹{amount:.2f}')


    total_spent = sum([expense.amount for expense in expenses])
    # This line calculates the total amount spent by summing up the amount attribute of each expense object in the expenses list

    print(f'💸 You have spent ₹{total_spent:.2f} this month')
    #                                    ^ :.2f keeps floating number as 2 digits only. Ex : 100.34

    remaining_budget = budget - total_spent
    print(f'💰 Remaining budget : ₹{remaining_budget:.2f}')


def view_all_expenses():
    expenses = get_all_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\nID | NAME | AMOUNT | CATEGORY")
    print("-" * 45)

    for exp in expenses:
        print(f"{exp.id} | {exp.name} | ₹{exp.amount:.2f} | {exp.category}")


def view_expense_by_id():
    expense_id = int(input("Enter expense id: "))

    row = get_expense_by_id(expense_id)

    if not row:
        print("Expense not found.")
        return

    id, name, amount, category = row
    print("\nExpense Found:")
    print(f"ID: {id}")
    print(f"Name: {name}")
    print(f"Amount: ₹{amount:.2f}")
    print(f"Category: {category}")


    #  LOGIC CODE TO SHOW HOW MUCH YOU CAN SPEND EACH DAY TILL END OF MONTH

    # Get the current date
    now = datetime.datetime.now()
    # Get the num on days in current month
    days_in_month = calendar.monthrange(now.year , now.month)[1]
    # Calc remaning num of days in current month
    remaining_days = days_in_month - now.day

    print('🗓️ Remaining days in current month: ', remaining_days)

    daily_budget = remaining_budget / remaining_days # type: ignore
    print(f'👉 Budget per day : ₹{daily_budget:.2f}')


if __name__ == '__main__':
    # ^ this condition checks if we are running it manually and will only work if we are
    main()

