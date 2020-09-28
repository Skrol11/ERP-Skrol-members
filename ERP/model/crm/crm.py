""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util
import csv


DATAFILE = "model/crm/crm.csv"#gdyby nie działało ./ na początku
HEADERS = ["id", "name", "email", "subscribed"]


def read():
    list_cust = {}
    list_cust = data_manager.read_table_from_file(DATAFILE, separator=';')
    return list_cust


def write(list_cust):
    list_cust = {}
    data_manager.write_table_to_file(DATAFILE, separator=';')
    return list_cust
    
