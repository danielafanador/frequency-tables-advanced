opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

frequency_table = {}

def freq_table (column):
    
    for row in apps_data[1:]:
        
        input = row[column]
        
        if input in frequency_table:
            frequency_table[input] += 1
        else:
            frequency_table[input] = 1
            
    return frequency_table
        
ratings_ft = freq_table (7)

print (ratings_ft)