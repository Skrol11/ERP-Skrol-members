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
      
def write():
    data_manager.write_table_to_file(DATAFILE, SALES_DATABASE, separator=';')

def update(transaction_id, index, value):
    read()
    for i in SALES_DATABASE:
        if i[0] == transaction_id:
            i[int(index)] = value
    write()
            
def delete(transaction_id):
    read()
    for i in SALES_DATABASE:
        if i[0] == transaction_id:
            SALES_DATABASE.remove(i)
    write()

def convert_date(date_as_str):
    y,m,d = date_as_str.split("-")
    return [int(y), int(m), int(d)]

def get_biggest_revenue_sale():
    read()
    biggest_revenue_sale = max(SALES_DATABASE, key=lambda sale: sale[2])
    return biggest_revenue_sale[1]

#     - (5) Get the transaction that made the biggest revenue.

# def biggest_revenue_transaction():
#     read()
#     prices = []
#     for item in SALES_DATABASE:
#         prices.append(float)
    

#     - (6) Get the product that made the biggest revenue altogether.


#     - (7) Count number of transactions between two given dates.


#     - (8) Sum the price of transactions between two given dates.