
# Import Path acroos operating systems and CSV file
import os
import csv

#Create path for budget_data_csv file
budget_data_csv = os.path.join(r"C:\Users\Gabrellea\Downloads\Starter_Code (5)\Starter_Code\PyBank\Resources\budget_data.csv")


#Create the output of the text file
text_path = "output.txt"

#List variables
total_months = 0
total_profit = 0
monthly_profit_change = 0
previous_profit = 0
change_list = []
month_of_change = []
profit = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
profit_average = 0



#open the budget_data_csv file
with open(budget_data_csv) as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #Loop through looking for total number of months
    for row in csvreader:

         #Count total months
        total_months += 1

        #Calculate the total profit over the entire period
        total_profit = total_profit + int(row["Profit/Losses"])

        #Calculate the average change in profit between months over the entire period
        monthly_profit_change = int(row["Profit/Losses"])- previous_profit
        previous_profit = int(row["Profit/Losses"])
        change_list = change_list + [monthly_profit_change]
        month_of_change = [month_of_change] + [row["Date"]]
       
       

        #The greatest increase in profit (date and amount) over the entire period
        if monthly_profit_change>greatest_increase[1]:
            greatest_increase[1]= monthly_profit_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in profit (date and amount) over the entire period
        if monthly_profit_change<greatest_decrease[1]:
            greatest_decrease[1]= monthly_profit_change
            greatest_decrease[0] = row['Date']
    profit_average = sum(change_list)/len(change_list)

#write financial analysis
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total: $%d\n" % total_profit)
    file.write("Average Change $%d\n" % profit_average) 
    file.write("Greatest Increase in profit: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in profit: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))