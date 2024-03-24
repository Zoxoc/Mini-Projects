import os
expenses = {}
income = {}
choice = 0
user_name = input("Your Name: ")
account_start = float(input("Enter your balance(in numbers): "))
balance = account_start
print("\n----MENU----\n")
print("1.Income\n2.Expense\n3.Balance Amount\n4.Expenses List\n5.Exit\n")
while choice != 5:
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        income_amt = float(input("\nIncome Amount: "))
        source_income = input("Source of Income: ")
        # stores the income amt and source to a dictionary
        income[f'{source_income}'] = income_amt
        balance += income_amt  # updating balance
    elif choice == 2:
        expense_amt = float(input("\nExpenditure Amount: "))
        source_expense = input("Purpose/Source of Expenditure: ")
        # stores the expense amt and purpose in a dictionary
        expenses[f'{source_expense}'] = expense_amt
        balance -= expense_amt  # updating balance
    elif choice == 3:
        print(f"\nYour Name: {user_name}")
        print(f"Starting Balance: {account_start}")
        print(f"Current Balance: {balance}")
    elif choice == 4:
        # to create a table ({:<10} means 10 spaces to the right)
        print("{:<10} {:<10}".format('Purpose', 'Amount'))
        for key, value in expenses.items():  # going through each expense purpose and its amt in the dictionary we stored
            Purpose = key
            Amount = value
            print("{:<30} | {:<30}".format(Purpose, Amount))
    elif choice == 5:
        print("\nThank You for using our budget tracker.\n")
        feedback = input(
            # filepath of the feedback file
            "Please Give us your Feedback to improve our budget tracker: ")
        filepath = "/Users/madhav/Desktop/Projects/Python/Mini Projects/feedback_budget_tracker.txt"
        # checks if the file is present in the specific location and return True or False
        file_check = os.path.isfile(filepath)
        if file_check == True:
            with open(filepath, "a") as f:
                f.write(f"{user_name}: {feedback}\n\n")
        else:
            with open(filepath, "w") as f:
                f.write(f"{user_name}: {feedback}\n\n")
        exit()
