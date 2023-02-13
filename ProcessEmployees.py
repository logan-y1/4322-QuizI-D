'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open('employee_data.csv', 'r')
reader = csv.reader(infile)
next(reader)


#create an empty dictionary
new_dict = {}

#use a loop to iterate through the csv file
i = 0
for row in infile:
     employee_id = row[0]
     first_name = row[1]
     last_name = row[2]
     salary = row[5]

     print('Manager Name:', first_name + ' ' + last_name, 'Current Salary:', salary)
    
    #check if the employee fits the search criteria

    if employee_id in infile:
     new_dict = {
          'id' : employee_id,
          'first name' : first_name,
          'last name' : last_name,
          'salary' : salary*1.1
     }
     i += 1

    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout

for i in new_dict.items():
     print('Manager Name:', new_dict['first name'] + ' ' +  new_dict['first name'], 'Current Salary:', new_dict['salary'])
     print()
infile.close         
        

        
    
