
#John Garcia
#Conversion Calculator for Project 5 H&S



def binary_to_decimal(number):
    result = 0
    if len(number) > 0: #uses length for function
        power = len(str(number)) - 1
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1

    return result #gives back result value

def DecimalToBinary(num): #converts decimal number to binary and returns the number
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
    return num

def DecimalToOctal(num): #converts decimal number to octal and returns the number
    if num >= 1:
        DecimalToOctal(num // 8)
    print(num % 8, end = '')
    return num

def HexToDecimal(hex_string):
    return int(hex_string, 16)

def DecimalToHex(num):
    return hex(num)[2:] #uses hex function for conversion || 2: removes the 0b at the start

def HexToBinary(hex_num):
    hex_num = HexToDecimal(hex_num)
    hex_num = DecimalToBinary(hex_num)
    binary = hex_num
    return binary

def BinaryToHex(binary):
    binary = binary_to_decimal(binary)
    binary = DecimalToHex(binary)
    hex_num = binary
    return hex_num




def main():

    print("Welcome to My Number Conversion Program")
    pick = 0
    while (pick == 0): #loop so the program continues
        pick = int(input(" Enter 1 to exit program \n Enter 2 for Binary to decimal \n Enter 3 for Decimal to Binary \n Enter 4 for Decimal to Octal \n Enter 5 for Hexadecimal to Decimal \n Enter 6 for Decimal to Hexadecimal \n Enter 7 for Hexadecimal to Binary \n Enter 8 for Binary to Hexadecimal \n "))
 #gives the user their options with the program how to pick them ^
        if (pick ==  2):
            num = input("Input binary number:")
            print("Your decimal number is: \n {}".format(binary_to_decimal(num))) #prints line and
            pick = pick - 2 #sends the loop back to the start

        elif (pick == 3):
            num = int(input("Input decimal number:"))
            print("Your binary number is:")
            (DecimalToBinary(num))
            print("\n")
            pick = pick - 3

        elif (pick == 4):
            num = int(input("Input decimal number:"))
            print("Your octal number is:")
            (DecimalToOctal(num))
            print("\n")
            pick = pick - 4

        elif (pick == 5):
            hex_string = input("Input hexadecimal number: ")
            decimal_number = HexToDecimal(hex_string)
            print("Your decimal number is:", decimal_number)
            print("\n")
            pick = pick - 5

        elif (pick == 6):
            num = int(input("Input decimal number: "))
            hex_num = DecimalToHex(num)
            print("Your hexadecimal number is:", hex_num)
            print("\n")
            pick = pick - 6

        elif (pick == 7):
            hex_num = input("Input hexadecimal number: ")
            print("Your binary number is: ")
            binary_num = HexToBinary(hex_num)
            print("\n")
            pick = pick - 7

        elif (pick == 8):
            num = input("Input binary number:")
            binary = BinaryToHex(num)
            print("Your hexadecimal number is:", binary)
            print("\n")
            pick = pick - 8


        elif (pick == 1): #gives the user a way to exit the program
            print("Goodbye!")
            pick = pick - 2
            break

    else: #stops the user from entering an invalid selection
        print("Invalid Entry")




if __name__ == "__main__": #starts the program
    main()
