import csv
import os
import datetime

from user_input import get_args
from input_validation import *

DB_NAME = 'DB.csv'
FIELDS_ROW = ['ID', 'Date', 'Description', 'Amount']


# main action selection
def main():
    args = get_args()

    match args.action:
        case 'add':
            if add_expense(args):
                print('The expense added successfully')
            else:
                print('The expense was not added.')

        case 'list': print_expenses()
        case 'summary': print_summary(args)  # by month or generic
        case 'delete':
            if delete_expense(args):
                print('The expense deleted successfully')
            else:
                print('No expense was written off.')
        case 'update':
            if update(args):
                print('The expense updated successfully')
            else:
                print('No expense was updated.')


# update an existing task, return if expense was updated
def update(args) -> bool:
    # check if DB_exist before updating an expense
    if not DB_exist():
        print('ERROR: task must be added before updating.')
        return False

    if not is_valid_amount(args.id):
        print('ERROR: id is not provided.')
        return False

    # fetch content from DB file to data as 2d array
    data = get_DB()

    return True


# print summary of expenses by month if provided or generic otherwise
def print_summary(args):
    if not DB_exist():
        print(0)
        return

    if args.month is None:
        print(sum_expenses())
    else:
        total = sum_expenses_by_month(int(args.month))
        print(f'Total expenses: ${total}')


# return the sum of expenses in a given month
def sum_expenses_by_month(month) -> int:
    total = 0
    with open(DB_NAME, 'r') as csv_file:
        csv_dictreader = csv.DictReader(csv_file)
        for row in csv_dictreader:
            date_str = row['Date']
            date_arr = date_str.split('/')
            curr_month = int(date_arr[0])

            if (curr_month == month):
                curr_amount = int(row['Amount'])
                total = total + curr_amount

    return total


# delete an expense, return if expense deleted successfully
def delete_expense(args) -> bool:
    # check if DB exist before deleting
    if not DB_exist():
        print('ERROR: expense must be added before deletion')
        return False

    # if id is missing
    if not is_arg_provided(args.id):
        print('ERROR: id is missing.')
        return False

    id = int(args.id)

    # fetch DB content to data as a 2d array
    data = get_DB()

    # check if id is in valid range
    if not is_valid_id(id, len(data)):
        print('ERROR: id is out of range.')
        return False

    # delete the line
    del data[id]

    # decrease by one the indexes that greater that id number
    decrease_indexes(data, id)

    # rewrite DB after changes
    write_DB(data)

    return True


# decrease the indexes of expences in DB, starts from a given number (id)
def decrease_indexes(data, start):
    for i in range(start, len(data)):
        curr_index = int(data[i][0])
        data[i][0] = curr_index - 1


# return the sum of all expenses
def sum_expenses():
    total = 0
    with open(DB_NAME, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            total = total + int(row[3])

    return total


# print all expenses
def print_expenses():
    # check if DB_exist before printing
    if not DB_exist():
        return
    with open(DB_NAME, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)


# add expense to DB, return if expense added successfully
def add_expense(args) -> bool:
    # check if DB_exist before adding an expense
    if not DB_exist():
        create_DB()

    id = get_last_ID() + 1
    date = datetime.datetime.now().strftime("%x")
    amount = 0 if args.amount is None else int(args.amount)

    if not is_valid_amount(amount):
        print('ERROR: amount must be non negative.')
        return False

    new_row = [id, date, args.description, amount]

    with open(DB_NAME, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(new_row)

    return True


# return the number of expenses in DB
def get_last_ID() -> int:
    if not DB_exist():
        return -1

    with open(DB_NAME, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        return sum(1 for row in csv_reader) - 1


# checks if DB.csv file exist
def DB_exist() -> bool:
    return os.path.isfile(DB_NAME)


# create DB file if not exist
def create_DB():
    # check if DB file already exist
    if DB_exist():
        return
    with open(DB_NAME, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(FIELDS_ROW)


# return csv content as a 2d array
def get_DB() -> list:
    data = []
    # read and store all data from DB
    with open(DB_NAME, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)

    return data


# rewrite DB file to given 2d content array
def write_DB(data):
    with open(DB_NAME, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)


if __name__ == '__main__':
    main()
