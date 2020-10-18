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


#     - (5) Get the transaction that made the biggest revenue.
def get_biggest_revenue_sale():
    read()
    maximum = 0
    i_max = ""
    for i in SALES_DATABASE:
        if maximum < float(i[3]):
            maximum = float(i[3])
            i_max = i
    return i_max
        
#     - (6) Get the product that made the biggest revenue altogether.        
def get_biggest_revenue_product():
    read()
    słownik = {}
    maximum = 0
    for i in SALES_DATABASE:
        if i[2] in słownik:
            słownik[i[2]] += float(i[3])
        else:
            słownik[i[2]] = float(i[3])
    print(słownik)
    for j in słownik:
        if maximum < słownik[j]:
            maximum = float(słownik[j])
    print(maximum)




#     - (7) Count number of transactions between two given dates.


#     - (8) Sum the price of transactions between two given dates.