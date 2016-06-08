#The football.csv file contains the results from the English Premier League. 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv


def read_data(filename):
    """
    Takes a csvfile and returns a list of dictionaries
    """
    
    data_list=[]

    with open(filename, 'rb') as footfile:
        footreader = csv.DictReader(footfile, delimiter = ",")
        for row in footreader:
            data_list.append(row)
    
    return data_list

def get_min_score_difference(parsed_data):
    """
    Takes a list of dictionaries and sorts the list by the difference in goals
    """
    new_list = sorted(parsed_data, key = lambda x: abs(int(x['Goals'])-int(x['Goals Allowed'])))
    # code for checking output of sorted list
    #for i in new_list:
    #    print i['Team'], abs(int(i['Goals'])-int(i['Goals Allowed']))
    return new_list

def get_team(parsed_data):
    """
    Takes the sorted list of dictionaries and returns the team in the first element
    """
    return parsed_data[0]['Team']

filename = 'football.csv'
foot_data = read_data(filename)
sorted_foot_data = get_min_score_difference(foot_data)
print get_team(sorted_foot_data)
