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

# from csv import writer

# with open('fille1.csv','w') as f:

#     csv_writer= writer(f)

#     csv_writer.writerow(['name','age'])

#     csv_writer.writerow(['sandeep','20'])

#     csv_writer.writerow(['sohail','19'])


#     csv_writer.writerows([['name','age'],['sandeep','20'],['sohail','20'],['khushal','19']])


    # 8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888


    # A csv stands for "comma separated values", which is defined as a simple file format that uses specific structuring to arrange tabular data. It stores tabular data such as spreadsheet or database in plain text and has a common format for data interchange. A csv file opens into the excel sheet, and the rows and columns data define the standard format.


import csv    
with open('python.csv') as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')    
    line_count = 0    
    for row in csv_reader:    
        if line_count == 0:    
            print(f'Column names are {", ".join(row)}')    
            line_count += 1




# e CSV module work is used to handle the CSV files to read/write and get data from specified columns. There are different types of CSV functions, which are as follows:

# csv.field_size_limit - It returns the current maximum field size allowed by the parser.
# csv.get_dialect - It returns the dialect associated with a name.
# csv.list_dialects - It returns the names of all registered dialects.
# csv.reader - It read the data from a csv file
# csv.register_dialect - It associates dialect with a name. The name must be a string or a Unicode object.
# csv.writer - It writes the data to a csv file
# o csv.unregister_dialect - It deletes the dialect which is associated with the name from the dialect registry. If a name is not a registered dialect name, then an error is being raised.
# csv.QUOTE_ALL - It instructs the writer objects to quote all fields. csv.QUOTE_MINIMAL - It instructs the writer objects to quote only those fields which contain special characters such as quotechar, delimiter, etc.
# csv.QUOTE_NONNUMERIC - It instructs the writer objects to quote all the non-numeric fields.
# csv.QUOTE_NONE - It instructs the writer object never to quote the fields.
