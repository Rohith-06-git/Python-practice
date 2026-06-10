expense = input("Enter expense: ")

with open("expenses.txt", "a") as file:
    file.write(expense + "\n")

print("\nExpense History:")

with open("expenses.txt", "r") as file:
    data = file.read()
    print(data)