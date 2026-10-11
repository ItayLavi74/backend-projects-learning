from user_input import get_args
import csv
import os
import datetime
import pprint

DB_NAME = 'DB.csv'
FIELDS_ROW = ['ID', 'Date', 'Description', 'Amount']


def main():
    args = get_args()

    match args.action:
        case 'add': add_expense(args)
        case 'list': show_expenses()
        case 'summary': sum_expenses()
        case 'delete': delete_expense(args)


def delete_expense(args):
    if not DB_exist():
        return

    # if id is missing
    if args.id is None:
        print('ERROR: id is missing.')
        return

    data = []
    id = int(args.id)

    if id < 1:
        print('ERROR: id must be greater that 1.')
        return

    # read and store all data from DB
    with open(DB_NAME, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)

    # delete the line
    del data[id]

    # decrease by one the indexes that greater that id number
    decrease_indexes(data, id)

    # rewrite DB after changes
    with open(DB_NAME, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)


def decrease_indexes(data, id):
    for i in range(id, len(data)):
        curr_index = int(data[i][0])
        data[i][0] = curr_index - 1


def sum_expenses():
    if not DB_exist():
        return
    total = 0
    with open(DB_NAME, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            total = total + int(row[3])

    print(f'Total expenses: ${total}')


def show_expenses():
    if not DB_exist():
        return
    with open(DB_NAME, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)


def add_expense(args):
    if not DB_exist():
        create_DB()

    id = get_last_ID() + 1
    date = datetime.datetime.now().strftime("%x")
    amount = 0 if args.amount is None else args.amount
    new_row = [id, date, args.description, amount]

    with open(DB_NAME, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(new_row)


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


# create DB if not exist
def create_DB():
    if DB_exist():
        return
    with open(DB_NAME, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(FIELDS_ROW)


if __name__ == '__main__':
    main()
