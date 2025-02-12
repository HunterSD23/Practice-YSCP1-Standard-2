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

def main():
    monthlyIncome = getMonthlyIncome()
    expenses = {}

    while True:    
        print("\n\n##############################################################")
        print("#####                                                    #####")
        print("###   Welcome to the Budget Planner and Expense Tracker!   ###")
        print("#####                                                    #####")
        print("##############################################################\n")
        print("What would you like to do?")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Quit\n")

        userChoice = int(input("Pick an option: "))
        if userChoice == 1:
            addExpense(expenses)
        elif userChoice == 2: 
            displaySummary(monthlyIncome, expenses)
        elif userChoice == 3:
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Try again.")

def getMonthlyIncome():
    while True:
        monthlyIncome = float(input("Enter Your Monthly Income: "))

        if monthlyIncome >= 0:
            return monthlyIncome
        else:
            print("Invalid input. Please enter a non-negative number.")

def addExpense(expenses):
    category = input("Enter the category of the expense: ")

    while True:
        amount = float(input("Please enter the expense amount: "))

        if amount >= 0:
            expenses[category] = expenses.get(category, 0) + amount
            print("Expense added.")
            break

def displaySummary(monthlyIncome, expenses):
    totalExpenses = sum(expenses.values())
    remainingBudget = (monthlyIncome - totalExpenses)

    print("Total Income: $", monthlyIncome)
    print("Expenses:")
    for category, amount in expenses.items():
        percentage = (amount / monthlyIncome) * 100
        print(f"{category}: $ {amount:.2f} ( {percentage:.2f} %)")

    print("Total Expenses: $", totalExpenses)
    print("Remaining Budget: $", remainingBudget)

"""
Code to start the application
"""
if __name__ == "__main__":
    main()