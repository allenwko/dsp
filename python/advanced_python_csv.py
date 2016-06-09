#PLACE YOUR CODE HERE

from collections import Counter
import csv

def csv_to_dict(filename):
    """Reads a CSV file to dictionary, returns a list of dictionaries"""
    data_list = []
    
    with open(filename, 'rb') as datafile:
        data_reader = csv.DictReader(datafile, delimiter = ',')
        for row in data_reader:
            data_list.append(row)

    return data_list

def email_list(listdict):
    email_list = []
    for i in listdict:
        email_list.append(i[" email"])
    return email_list

def email_csv(em_list):
    with open('email.csv', 'wrb') as f:
        writer = csv.writer(f)
        for i in em_list:
            writer.writerow([i])
        
fac_data = csv_to_dict('faculty.csv')
em_list = email_list(fac_data)
email_csv(em_list)
