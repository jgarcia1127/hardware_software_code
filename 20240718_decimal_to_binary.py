def binary_to_decimal(str_number):
    result = 0
    if len(str_number)>0:
        power = len(str_number)) - 1
        for num in str(str_number):
            result += int(num)*2 ** power
            power -= 1
            return result
def main():
    num = input("enter binary number:")
    print("Binary to Decimal :{}".format(binary_to_decimal(num)))

if __name__ == "__main__":
    main()
