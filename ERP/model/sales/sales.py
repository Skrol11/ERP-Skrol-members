""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "ERP/model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

SALES_DATABASE = []
ID_INDEX = 0
CUSTOMER_INDEX = 1
PRODUCT_INDEX = 2
PRICE_INDEX = 3
DATE_INDEX = 4

# 2. Implement the Sales module with basic and special operations.
#     - (1-4) Provide basic CRUD operations.

def read():
    global SALES_DATABASE
    SALES_DATABASE = data_manager.read_table_from_file(DATAFILE)

def create(Customer, Product, Price, Date):
    read()
    new_id = util.generate_id(number_of_small_letters=4, number_of_capital_letters=2, number_of_digits=2, number_of_special_chars=2, allowed_special_chars=r"_+-!")
    SALES_DATABASE.append([new_id, Customer, Product, Price, Date])
    data_manager.write_table_to_file(DATAFILE, SALES_DATABASE, separator=';')

# def update()

#     - (5) Get the transaction that made the biggest revenue.

#     - (6) Get the product that made the biggest revenue altogether.


#     - (7) Count number of transactions between two given dates.


#     - (8) Sum the price of transactions between two given dates.