from model.crm import crm
from view import terminal as view
import csv
import os



def list_customers():
    model.crm.read_customers()
    

# def add_customer():
#     with open(filepath, newline='') as file:
#         for row in csv.writer(file):
#             LIST_CUST.update(row)
#             for customer in LIST_CUST:
#                 if customer in LIST_CUST:
#                     return False
#                 else:
#                     LIST_CUST[customer] = 1
#                     return LIST_CUST


# def update_customer():
#     with open(filepath, newline='') as file:
#         for row in csv.writer(file):
#             LIST_CUST.update(row)
#             for customer in LIST_CUST:
#                 if customer in LIST_CUST:
#                     LIST_CUST[new_customer] = LIST_CUST.pop[customer]
#                     del LIST_CUST[customer]
#                     return LIST_CUST
#                 else:
#                     return False
    

# def delete_customer():
#     with open(filepath, newline='') as file:
#         for row in csv.writer(file):
#             LIST_CUST.update(row)
#             for customer in LIST_CUST:
#                 if customer in LIST_CUST:
#                     LIST_CUST.pop(customer)
#                     return LIST_CUST
#                 else:
#                     return False


# def get_subscribed_emails():
    
#     view.print_error_message("Not implemented yet.")


def display_menu():
    os.system("cls || clear")
    print('Customer Relationship Management')
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")





def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
