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

def dict_form1(fac_data):
    """ Takes list of dictionaries, returns dictionary """
    #sort through last names
        #count number last names? maybe not
    #create key for each last name
        #if key exists, add list of values [degree, title -'of biostatistics', email]
    
    form_dict = {}

    for i in fac_data:
        #get name
        split_name = i['name'].split(" ")
        last_name = split_name[len(split_name)-1]
        
        #build array of degree/title/email
        fixed_title = i[' title'].strip(" of Biostatistics")
        
        info = []
        info.append(i[' degree'])
        info.append(fixed_title)
        info.append(i[' email'])
        
        #add to dictionary
        if last_name in form_dict:
            form_dict[last_name].append([info])
        else:
            form_dict[last_name] = info

    return form_dict

def dict_form2(fac_data):
    """ Takes list of dictionaries, returns dictionary with 2nd format"""
    #sort through last names
    #create key for each last name
        #if key exists, add list of values [degree, title -'of biostatistics', email]
    
    form_dict = {}

    for i in fac_data:
        #get name
        split_name = i['name'].split(" ")
        last_name = split_name[len(split_name)-1]
        first_name = split_name[0]
        key = (last_name, first_name)
        
        #build array of degree/title/email
        fixed_title = i[' title'].strip(" of Biostatistics")
        
        info = []
        info.append(i[' degree'])
        info.append(fixed_title)
        info.append(i[' email'])
        
        #add to dictionary
        if key in form_dict:
            form_dict[key].append([info])
        else:
            form_dict[key] = info

    return form_dict

fac_data = csv_to_dict('faculty.csv')

first_dict = dict_form1(fac_data)
#print first 3 items in first format
for i in range(3):
    print first_dict.items()[i]
print "\n"

second_dict = dict_form2(fac_data)

for i in range(3):
    print second_dict.items()[i]
print "\n"

nameslist=[]
#print second dictionary in alpha order by last name
for i in second_dict:
    nameslist.append(i)

nameslist = sorted(nameslist, key = lambda x: x[0])

for i in nameslist:
    print i, ":", second_dict[i]
