from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def get_menu():
    menu_dict = {
    '1' : 'Decimal2Binary',
    '2' : 'Binary2Decimal',
    'x' : 'exit_program'
    }
    return menu_dict

def display_menu(menu_dict):
    print('\t\t\tConversion Calculator')
    print('')
    for items, values in menu_dict.items():
        print('\t\t{}. {}'.format(items, values.replace('-', ' ').capitalize()))
    menu_selection = input("\n\t\tEnter Selection: ").lower()
    return (menu_dict.get(menu_selection, "invalid_entry"))

def Decimal2Binary():
    num = input("Please enter your decimal")
    if num >= 1:
         num // 2
         print(num % 2, end = '')
def Binary2Decimal():
    input("You selected bananas.")
def invalid_entry():
    input("Invalid Entry!!")
def exit_program():
    input("Good Bye!!!")
    return 'true'

def main():
    done_selecting = 'false'
    while done_selecting != 'true':
        clear_screen()
        get_selection = display_menu(get_menu())
        done_selecting = eval(get_selection+"()")

if __name__ == "__main__":
    main()
