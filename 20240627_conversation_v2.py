def conversation():
    print("We want to know if you like programming!")
    print("What is your name?")
    name = input()
    print("Do you like programming " + name + "?")
    answer = input()
    print("Great! you said,", answer)
    print("Let's learn some Python today!!! ")

def main():
 conversation()

if __name__ == "__main__":
    main()
