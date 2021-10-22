import csv
from hashlib import md5

def count_number_of_entries_in_csv(filename):

    with open(filename, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        row_count = sum(1 for row in csv_reader)

    return row_count


def get_hash_of_csv(filename):

    with open(filename, 'rb') as csv_file:
        csv_reader = csv_file.read()
        csv_hash = md5(csv_reader).hexdigest()

    return csv_hash


def write_hash_of_csv(filename, csv_hash):

    with open(filename, 'w') as realty_hash_file:
        realty_hash_file.write(str(csv_hash))


def read_hash_of_csv(filename):

    with open(filename) as csv_hash_file:
        csv_hash = csv_hash_file.read()
    return csv_hash
