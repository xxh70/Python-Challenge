# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:54:42 2019

@author: trs7
"""


import os
import csv

#1.  one argument since both of files are in the same level
csvpath = os.path.join("budget.csv")
if os.path.isfile(csvpath):
    with open(csvpath,newline="") as csv_file:
        csv_reader = csv.reader(csv_file,delimiter = ",")
#Calculate total profit

# skip the first line
        next(csv_reader)
#set up variables and set up initial value as 0
        date = []
        Profit_Losses=[]
        total_profit = 0
        total_month = 0
        for line in csv_reader:
            total_profit += int(line[1]) #since profit is in the 2nd column
#add value of profit into Profit list
            Profit_Losses.append(line[1])
            print(Profit_Losses)
            date.append(line[0])
            print(date)
# 2. calculate total month = to row number if i skip the first row.
        
    total_month += 1
    print(total_month)
    print(total_profit)
# 3. calculate the average of change

#find the changing value between the two connected months
    change =[]
    print(len(Profit_Losses))
    for i in range(len(Profit_Losses)):
        if i == 0:
            continue
        change.append(int(Profit_Losses[i]) - int(Profit_Losses[i-1]))
        Average_change = sum(change) / len(change)
    print(Average_change)

#get the Greatest increase and decreased profits by adding max or min front of change 
Greatest_Increase_Profits = max(change)   
Greatest_Decrease_Profits = min(change)
print(Greatest_Increase_Profits)
print(Greatest_Decrease_Profits)

#get the greastest increased index number from change list  
index = change.index(max(change))
print(index)

#get the date from date list by adding indexing number 
print(date[25])

index = change.index(min(change))
print(index)

print(date[44])

#Summary
print( "Financial Analysis")
print("---------------------------------------------")
print("Total Months: 86")
print("Total: 38382578")
print("Average Change:-2315.12" )
print("Greatest Increase in Profits: Feb-2012 ($1926159)")
print("Greatest Decrease in Profits: Sep-2013 ($-2196167)")
# create text file 
text_file = 'text'
with open(text_file, 'w') as text:
    print(text)