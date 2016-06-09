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

def field_freq(listdict, field):
    """
    Takes a list of dictionaries and a field
    Returns frequency of each element, and amount of unique elements
    """
    fieldlist = []
    for i in listdict:
        fieldlist.append(i[field])
    #print Counter(fieldlist)
    return Counter(fieldlist)

def email_list(listdict):
    email_list = []
    for i in listdict:
        email_list.append(i[" email"])
    return email_list

def count_email_domains(listdict):
    domain_list = []
    for i in listdict:
        at_index = i[' email'].find("@")
        len_i = len(i[' email'])
        domain_list.append(i[' email'][at_index:len_i])

    return Counter(domain_list)

fac_data = csv_to_dict('faculty.csv')
print field_freq(fac_data, ' degree')
print field_freq(fac_data, ' title')
print email_list(fac_data)
print count_email_domains(fac_data)
