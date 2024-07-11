def conversation(name):
    print("Welcome to my conversation program!!!")
    print("Glad to have you in h&s")
    return name

def question(name):
    print("We want to know if you like programming")
    answer = input("{}, do you like programming?".format(name.capitalize()))
    return answer

def check_response(response):
    response = response.strip()
    if response.lower() == "yes":
        print("Great! You said {}".format(response))
    else:
        print("Sorry to hear that")

def main():
    name = conversation(input("what is your name?"))
    your_answer = question(name)
    check_response(your_answer)
    print("Nice talking with you {}".format(name))

if __name__ == "__main__":
    main()
  
