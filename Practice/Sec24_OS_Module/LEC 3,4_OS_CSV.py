# LECTURE 03:

# # CSVRead.py:
# import csv

# f = open('EmployeeAdd.csv', 'r')
# csv_reader = csv.reader(f)

# next(csv_reader)  # It help in skipping the line



# sal = []
# for row in csv_reader:
#     # print(row)   # give all data for reading
#     # print(row[2]) # it give particular data to read 
#     # print(int(row[2])) # convert particular data into integer

#     sal.append(int(row[2]))
# print(sal)
# print('Min',min(sal))    # We can get maximum and minimum salary from file
# print('Max',max(sal))    # We can get maximum and minimum salary from file




#CSVDictReader:

import csv
import pprint   # Use this module to beautify the program  (p means preety) . use to print very large data in beatiful formatted way:

f = open('EmployeeAdd.csv', 'r')
csv_dict_reader = csv.DictReader(f)

dict1 = {}
for row in csv_dict_reader:

    # print(row)

    dict1[row['Joining Date']]=row
pprint.pprint(dict1)
# print('Ben',dict1['Ben'])
f.close()