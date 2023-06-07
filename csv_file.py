# from csv import reader

# with open ('file.csv', 'r') as f:

#     csv_reader= reader(f)

#     # next(csv_reader)

#     for row in csv_reader:

#         print(row)


# 8888888888888888888888888888888888888888888888888888888888888888888888888888888888888

from csv import DictReader

with open('file.CSV','r') as f:

    csv_reader = DictReader(f)

    for row in csv_reader:
        print(row)