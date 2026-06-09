def fun(x):
    if x % 2 == 0 :
        return "even"
    return "odd"
def evenorodd():
    print("check whether a number is even or odd")

    while True:
        choice = input("Enter 's' to stay and 'q' to quit :")
        if choice.lower() == 'q':
           print("Have a good Day")
           break
        else:
            num = int(input("Enter the Number :"))
            print(fun(num))

if __name__ == "__main__":
   evenorodd()
        


