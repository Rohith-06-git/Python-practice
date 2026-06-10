def factorial(x) :
    y = 1
    for i in range(1, x + 1):
        y = y * i
    return y
def display():
    print("Welcome to Factorial corner !!")
    try :
        z = int(input("Enter your number to find its factorial : "))
        print(factorial(z))
    except ValueError:
        print("Invalid Input")

if __name__ == "__main__" :
    display()