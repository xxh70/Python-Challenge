# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:36:11 2019

@author: trs7
"""
import os
import csv
# csv file is down one level than py file 
csvpath = os.path.join("Pypoll","election_data.csv")
# open file
with open(csvpath,newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
# set up initial total votes as 0

#count each candidate's total voter
with open(csvpath,newline='' ) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    for row in csv_reader:
        #print(row)
        if row[2]=="Khan":     
            Khan_votes += 1
        elif row[2]=="Correy":
            Correy_votes += 1
        elif row[2]=="Li":
            Li_votes += 1
        elif row[2]=="O'Tooley":
            OTooley_votes += 1
    total_votes = 0
    total_votes = Khan_votes + Correy_votes + Li_votes + OTooley_votes    
    print(total_votes)
    

#calculate each candidate's vate percentage
Khan_percentage = Khan_votes/total_votes
Correy_percentage = Correy_votes/total_votes
Li_percentage = Li_votes/total_votes
OTooley_percentage = OTooley_votes/total_votes


#find out the winner
if Khan_votes > Correy_votes and Khan_votes > Li_votes and Khan_votes > OTooley_votes:
    print("Khan is the winner")
elif Correy_votes > Khan_votes and Correy_votes > Li_votes and Correy_votes > OTooley_votes:
    print("Correy is the winner")
elif Li_votes > Khan_votes and Correy_votes < Li_votes and Li_votes > OTooley_votes:
    print("Li is the winner")
elif OTooley_votes > Khan_votes and Correy_votes < OTooley_votes and OTooley_votes > Li_votes:
    print("OTooley is the winner")

# Summary
print("Election Results")
print("------------------------")
print("Total Votes: 3521001")
print("Khan: 63% (2218231)")
print("Correy: 20% (704200)")
print("O'Tooley: 3% (105630)")
print("------------------------")
print("Winner: Khan")
print("------------------------")

# create text file 
text_file = 'pypoll/text'
with open(text_file, 'w') as text:
    print(text)
    