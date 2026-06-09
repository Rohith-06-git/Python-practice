def add(x,y):
    return x + y 
def subt(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return "error , division by zero is not possible"
    return x / y
def calculator():
    print(" Basic Calc")
    print("choose operation")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Mutliplication")
    print("4.Division")

    while True:
        choice = input("choose among (1,2,3,4) or 'q' to quit : ")
        if choice.lower() == 'q':
            print("Have a good Day")
            break 
        if choice in ('1','2','3','4') :
            try:
                x = float(input("Enter num1 : "))
                y = float(input("Enter num2 : "))
            except ValueError:
                print("invalid input")
                continue

            if choice == '1':
                print(add(x,y))
            elif choice == '2':
                print(sub(x,y))
            elif choice == '3':
                print(mul(x,y))
            elif choice == '4':
                print(div(x,y))
        else:
            print("invalid input")
if __name__ == "__main__":
    calculator()
