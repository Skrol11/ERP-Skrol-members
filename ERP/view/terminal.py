def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    b = 1
    print(title)
    for i in list_options[1:]:
        print(f"({b})", i)
        b += 1
    print("(0)",list_options[0])

    # print()
    # print(1,list_options[1])
    # print(2,list_options[2])
    # print(3,list_options[3])
    # print(4,list_options[0])

def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """

# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
    pass

def print_table(table, HEADERS):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    cell_sizes = [16, 16, 32, 16, 16]
    print()
    print('-'*(sum(cell_sizes) + (3*len(HEADERS)+1)))
    print('| ',end='')
    for index, element in enumerate(HEADERS): 
        print(element + ' '*(cell_sizes[index]-len(element)), end =' | ')
    print('')
    print('-'*(sum(cell_sizes) + (3*len(HEADERS)+1)))
    for row in table: 
        print('| ',end='')
        for index, element in enumerate(row): 
            print(element + ' '*(cell_sizes[index]-len(element)), end =' | ')
        print('')
        print('-'*(sum(cell_sizes) + (3*len(row)+1)))
    print()



def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(f"Give {label}: ")
    
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    inputs = []
    for i in labels:
        inputs.append(input(i))
    return inputs


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"Error {message}")
