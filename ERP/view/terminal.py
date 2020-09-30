import sys
import os


def print_menu(menu, options):
    print(menu)
    for element in range(1, len(options)):
        print(f'({element}) {options[element]}')
    print(f'(0) {options[0]}')
    

# """
#     Args:
#         title (str): the title of the menu (first row)
#         list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
# """
    


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/


def print_table(table, HEADERS):
    
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    cell_sizes = [16, 16, 32, 16, 16]
    print()
    print('-'*(sum(cell_sizes) + (3*len(HEADERS)+1)))
    print('| ',end='')
    for index, element in enumerate(HEADERS): 
        print(element + ' '*(cell_sizes[index]-len(element)), end =' | ')
    print('')
    print('-'*(sum(cell_sizes) + (3*len(HEADERS)+1)))
    for row in table: 
        print('| ',end='')
        for index, element in enumerate(row): 
            print(element + ' '*(cell_sizes[index]-len(element)), end =' | ')
        print('')
        print('-'*(sum(cell_sizes) + (3*len(row)+1)))
    print()


def get_input(label):
   option = input(f'{label}: ')
   return option


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"Error {message}")


def change_of_data():
    number = int(input('Please write a number of a customer: '))
    return number


