from datetime import datetime

date_format = "%d-%m-%Y"
TYPES = {'I': 'Income', 'E': 'Expense'}

def get_date(prompt, allowd_default=False):
    date_str = input(prompt)
    if allowd_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the transaction date in 'dd-mm-yyyy' format.")
        return get_date(prompt, allowd_default)

def get_amount():
    try:
        amount = float(input("Enter the transaction amount: "))
        if amount <= 0:
            raise ValueError("Transaction amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_type():
    type = input("Enter the transaction type ('I' for Income or 'E' for Expense): ").upper()
    if type in TYPES:
        return TYPES[type]

    print("Invalid transcation type. Please enter 'I' for Income or 'E' for Expense.")
    return get_type()

def get_description():
    return input("Enter a description for the transaction(optional): ")