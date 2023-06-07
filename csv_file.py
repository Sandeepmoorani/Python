# from csv import reader

# with open ('file.csv', 'r') as f:

#     csv_reader= reader(f)

#     # next(csv_reader)

#     for row in csv_reader:

#         print(row)


# 8888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# from csv import DictReader

# with open('file.CSV','r') as f:

#     csv_reader = DictReader(f)

#     for row in csv_reader:
#         print(row)



# 8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

from csv import writer

with open('fille1.csv','w') as f:

    csv_writer= writer(f)

    csv_writer.writerow(['name','age'])

    csv_writer.writerow(['sandeep','20'])

    csv_writer.writerow(['sohail','19'])


    csv_writer.writerows([['name','age'],['sandeep','20'],['sohail','20'],['khushal','19']])