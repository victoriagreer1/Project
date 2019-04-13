'''
Created on Mar 30, 2019

@author: ITAUser
'''
import json 
answer = 'yes'
while answer!='no':
    with open ("assignments_1.json", "r") as f_r:
        data = json.load(f_r)
    print("\n\n We have assignments for the following dates...")
    for i in data:
        print("\n" + i)
        
    ans= input("1. Find an assignment. \n2 Add assignment \n\n")
    if ans=='1':
        name = input("Enter assignment name:")
        print ("The assignment for {} is {}".format(name, data.get(name, "not in our database")))
    elif ans=='2':
        n = int(input("How many assignments do you want to add? (max 3 at a time)"))
        i = 0
        while i<n:
            print("\n Add assignment", i+1)
            new_name = input ("\n Enter the name:")
            new_birthday = input ("enter the due date (dd/mm/yyyy):")
            data[new_name] = new_birthday 
            with open("assignments_1.json", "w") as f_w:
                json.dump(data, f_w)
            print ("Assignment Added!")
            i+=1
    else: 
        print("\n Invalid Choice! ")
    answer = input ("\n Do you want to use the assignment organizer again (yes/ no):")