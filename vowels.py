def vowels(x) :
    count = 0 
    for ch in x.lower() :
        if ch in "aeiou" :
            count = count + 1
    return count
def display() :
    print("Welcome , try finding the no.of vowels in your text ")
    while True :
        try :
          y = input("Enter your text or 'q' to Quit : ")
          if y.lower() == 'q' :
            print("Thank you , Have a Good Day !!")
            break
          else :
            print("The no.of vowels in your text is :",vowels(y))
        except ValueError:
           print("Invalid Input ")

if __name__ == "__main__":
   display()


