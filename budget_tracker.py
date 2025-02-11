"""
    function main()
    display 'Welcome to the Budget Planner and Expense Tracker!'
    monthlyIncome = getMonthlyIncome()
    expenses = empty dictionary

    loop forever:
        display menu:
            1} Add an expense
            2} View budget summary
            3} Exit

        userChoice = read input
        if userChoice == 1:
            addExpense(expenses)
        elif userChoice == 2: 
            displaySummary(monthlyIncome, expenses)
        elif userChoice == 3:
            display 'Goodbye!'
            break
        else:
            display 'Invalid choice. Try again.'
"""

def getMonthlyIncome():
    while True:
        monthlyIncome = float(input())

        if monthlyIncome >= 0:
            return monthlyIncome
        else:
            print("Invalid input. Please enter a non-negative number.")

def addExpense(expenses):
    category = input("Enter the category of the expense: ")

    while True:
        amount = float(input("Please enter the expense amount: "))

        # if amount >= 0:

def displaySummary(monthlyIncome, expenses):
    totalExpenses = expenses
    remainingBudget = monthlyIncome - totalExpenses

    print(monthlyIncome)
    print("(supposed to print the categories and their respective amounts spent, along with percentages)")
    print(totalExpenses)
    print(remainingBudget)

def main():
    print("\n\n##############################################################")
    print("#####                                                    #####")
    print("###   Welcome to the Budget Planner and Expense Tracker!   ###")
    print("#####                                                    #####")
    print("##############################################################\n")

    monthlyIncome = getMonthlyIncome()
    # expenses = empty dictionary

    while True:
        print("What would you like to do?")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Quit")

        userChoice = int(input("Pick an option: "))
        if userChoice == 1:
            addExpense(expenses)
        elif userChoice == 2: 
            displaySummary(monthlyIncome, expenses)
        elif userChoice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


"""
Code to start the application
"""
if __name__ == "__main__":
    main()