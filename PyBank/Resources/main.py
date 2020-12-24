#PyBank 

import os 
import csv

csvpath = os.path.join('Resources','budget_data.csv')
output_path = os.path.join("Output", "Election Results.txt")

print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csvheader = next(csvreader)
    print(csvheader)
  
  
    #financial analysis

    #total number of months
    #total profits and losses
    #avg changes in profits/losses over whole period
    #greatest increase in profits date and amount
    #greatest decrease in losses date and amount
   
    
   #total number of months
    months = 0
    list_of_months = []
    sum_profit_loss = 0
    row_count = 0
    net_difference_list = []
    

    line = next(csvreader)
    print(line)
    months = months + 1
    sum_profit_loss = sum_profit_loss + int(line[1])
    previous_value = int(line[1])
    total_row_avg = 0
    total = 0
    total_change = 0
    profits = []
    dates = []

    # loop through row 2 onwards
    for row in csvreader:
        months = months + 1
        current_row_value = int(row[1])
        sum_profit_loss = sum_profit_loss + current_row_value
        change = current_row_value - previous_value
        print(change)
        previous_value = current_row_value
        net_difference_list.append(change)
        list_of_months.append(row[0])

        total = total + int(row[1]) - previous_value
        total_row_avg = total_row_avg + 1
        total_change = total_change + change
        
        #print(total/total_row_avg)
        row_count = row_count + 1
    
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    greatest_decrease = min(profits)
    lowest_index = profits.index(greatest_decrease)
    lowest_date = dates[lowest_index]

    average_change = sum(profits)/len(profits)


    report_data = f"""
    Total =  {sum_profit_loss}
    Total Months = {months}"""
    print(report_data)
    print(months)
    print(total_change / months)
    #total profits and losses




# print("Financial Analysis")
# print("Total Months:" +str(list_of_months))
# print("Total Revenue:" + "$" + str(sum_profit_loss))
# print("Average Change:" + str())


file_output = open("budget_analysis.txt", "w")



        

#write_file = open(os.path.join("put file here".txt), 'w+')
#write_file.write("write into the file everything you print")







#pathToWriteFile = os.path.join("Resources", "output.txt")
#write_file = open(pathToWriteFile, 'w+')
# insert logic code here
#print("winners???")
#write_file.write("write into the file everything you print")
    