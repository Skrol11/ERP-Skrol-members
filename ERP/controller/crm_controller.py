from model.crm import crm
from view import terminal as view
import csv
import os


def list_customers():
    crm.read()
    view.print_table(crm.LIST_CUST, crm.HEADERS)


def add_customer():
    new_cust = view.get_input(crm.HEADERS[1])
    new_cust1 = view.get_input(crm.HEADERS[2])
    new_cust2 = view.get_input(crm.HEADERS[3])
    crm.write(new_cust, new_cust1, new_cust2)
    crm.read()
    view.print_table(crm.LIST_CUST, crm.HEADERS)
    


def update_customer():
    crm.read()
    view.print_table(crm.LIST_CUST, crm.HEADERS)
    number = view.change_of_data()
    if number - 1 <= len(crm.LIST_CUST):
        element = crm.LIST_CUST[number-1]
        user_choise = int(view.get_input("For update\n1. Name\n2.Email\n3.Subscribtion"))
        user_input = view.get_input("Please write new value: ")
        if user_choise == 1:
            crm.update(element[0], user_input, element[2], element[3])

        
def delete_customer():
    crm.read()
    view.print_table(crm.LIST_CUST, crm.HEADERS)
    number = view.change_of_data()
    if number - 1 <= len(crm.LIST_CUST):
        element = crm.LIST_CUST[number-1]
        crm.delete(element)
        crm.read()
        view.print_table(crm.LIST_CUST, crm.HEADERS)
        return
    else:
        print("Incorrect number")



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
