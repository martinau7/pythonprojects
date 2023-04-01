import sys

expenses = []

try:
    with open('expenses.txt', 'r') as f:
        expenses = eval(f.read())
except:
    pass


def remExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove? ")
        expenseToRemove = int(input("> "))
        if expenseToRemove < 0:
            print("Enter a existing expense number. ")
        try:
            del expenses[expenseToRemove]
            break
        except:
            print("Invalid input. Please try again. ")


def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)


def printMenu():
    print("Choose one of the following options: \n")
    print("1. Add a new expense. ")
    print("2. List all expenses to-date. ")
    print("3. Choose an expense to remove. ")
    print("4. Close the expense tracker. ")


def listExpenses():
    print("Here is a list of all your expenses: ")
    print("-------------------------------------")
    counter = 0
    for expense in expenses:
        print("Expense number ", counter, "  -  ", expense['category'], "  -  ", expense['amount'])
        counter += 1
        print("\n")


if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")
        if optionSelected == "1":
            print("How much did the expense cost? ")
            while True:
                try:
                    amountToAdd = input("> ")
                    break
                except:
                    print("Invalid input. Please try again. ")

            print("What category was the expense? ")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                    print("Invalid input. Please try again. ")

            addExpense(amountToAdd, category)

        elif optionSelected == "2":
            listExpenses()
        elif optionSelected == "3":
            remExpense()
        elif optionSelected == "4":
            with open('expenses.txt', 'w') as f:
                f.write(str(expenses))
            sys.exit()
        else:
            print("Invalid input. Please try again. ")
