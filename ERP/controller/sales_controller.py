from model.sales import sales
from view import terminal as view

def list_transactions():
    # view.print_error_message("Not implemented yet.")
    sales.read()
    view.print_table(sales.SALES_DATABASE, sales.HEADERS)
def add_transaction():
    # view.print_error_message("Not implemented yet.")
    inputs = view.get_inputs(["Give Customer: ", "Give Product: ", "Give Price: ", "Give Date: "])
    sales.create(inputs[0], inputs[1], inputs[2], inputs[3])

def update_transaction():
    transaction_id = view.get_input("Provide a valid transactions id to update profile")
    index = view.get_input("Specify which value you are attempting to change:\n1 for Customer, 2 for Product, 3 for Price, 4 for Date")
    value = view.get_input("Provide a new value for the selected category")
    sales.update(transaction_id, index, value) 
    # view.print_error_message("Not implemented yet.")

def delete_transaction():
    transaction_id = view.get_input("Provide a valid transactions id to update profile")
    sales.delete(transaction_id)
    # view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    biggest_transaction_revenue = sales.get_biggest_revenue_sale()
    view.print_general_results(biggest_transaction_revenue, "The biggest revenue transaction is: ")
    # view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
