""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util
import csv


DATAFILE = "ERP/model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
LIST_CUST = []
ID_INDEX = 0
NAME_INDEX = 1
EMAIL_INDEX = 2
SUBSCRIBED_INDEX = 3
LIST_SUBSCRIBED = []


def read():
    global LIST_CUST
    LIST_CUST = data_manager.read_table_from_file(DATAFILE)
    

def write(name, email, subscribed):
    read()
    new_id = util.generate_id(number_of_small_letters=4, number_of_capital_letters=2, number_of_digits=2, number_of_special_chars=2, allowed_special_chars=r"_+-!")
    LIST_CUST.append([new_id, name, email, subscribed])
    data_manager.write_table_to_file(DATAFILE, LIST_CUST, separator= ';')


def delete(element):
    read()
    LIST_CUST.remove(element)
    data_manager.write_table_to_file(DATAFILE, LIST_CUST, separator= ';')


def update(id, name, email, subscribed):
    for element in LIST_CUST:
        if element[0] == id:
            element[1] = name 
            element[2] = email 
            element[3] = subscribed
            data_manager.write_table_to_file(DATAFILE, LIST_CUST, separator= ';')
            return


def get():
    global LIST_SUBSCRIBED
    for element in LIST_CUST:
        if element[3] == '1':
            LIST_SUBSCRIBED.append(element)