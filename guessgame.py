import random
def guessgame() :
    print("Welcome to the Guessing Game ")
    print("I have a number between 1 and 100 in my mind ")

    x = random.randint(1,101)
    attempts = 0 

    while True :
        try : 
            y = int(input("Guess the number : "))
            attempts = attempts + 1 
            if y < x :
                print("you'r low try higher ")
            elif y > x :
                print("you'r high try lower ")
            else :
                print(" Hurray you have guessed it ,congratulations ")
                break
        except ValueError:
            print("Invalid input ")

if __name__ == "__main__":
    guessgame()

