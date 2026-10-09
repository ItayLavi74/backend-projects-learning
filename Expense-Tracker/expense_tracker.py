from user_input import get_args
import csv
import os
import datetime

DB_NAME = 'DB.csv'
FIELDS_ROW = ['ID', 'Date', 'Description', 'Amount']


def main():
    args = get_args()

    match args.action:
        case 'add': add_expense(args)


def add_expense(args):
    if not DB_exist:
        create_DB()

    id = get_last_ID() + 1
    date = datetime.datetime.now().strftime("%x")
    new_row = [id, date, args.description, args.amount]

    # with open(DB_NAME, 'w') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     csv_writer.writerow(new_row)


# return the number of expenses in DB
def get_last_ID() -> int:
    if not DB_exist:
        return

    with open(DB_NAME, 'w' ,newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        return sum(1 for row in csv_reader) - 1


# checks if DB.csv file exist
def DB_exist() -> bool:
    return os.path.isfile(DB_NAME)


# create DB if not exist
def create_DB():
    if DB_exist:
        return
    with open(DB_NAME, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(FIELDS_ROW)


if __name__ == '__main__':
    main()
