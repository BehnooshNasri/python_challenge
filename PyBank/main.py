import csv
import os

#set the path

CSV_PATH = os.path.join("Resources", "budget_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# open and read the file 

with open(CSV_PATH, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    header = next(csv_reader)
    rows = list(csv_reader)
   
    print("Financial Analysis")
    print("----------------------------")
    #find the total number of months included in the dataset
    #find the net total amount of "Profit/Losses" over the entire period

    last_date = ""
    month_count = 0 
    net = 0 
    for row in rows:
        net += float(row[1])
        date = row[0]
        if date != last_date:
            month_count +=1
            last_date = date

    print(f"total months: {month_count}")
    print(f"total net: ${net}")
   

    # Find and print the changes in "Profit/Losses" over the entire period, and then the average of those changes

    total_changes = 0
    prev_amount = float(rows[0][1])
    for row in rows:
        profit_losses = float(row[1])
        row.append(profit_losses - prev_amount)
        total_changes += profit_losses - prev_amount
        prev_amount = profit_losses

    average_change = total_changes / (len(rows) - 1)

    print(f"Average Change:${average_change}")


    #Find the greatest increase in profits (date and amount) over the entire period
    #Find the greatest decrease in profits (date and amount) over the entire period

    highest_increase = 0
    highest_increase_date = ""
    highest_decrease = 0
    highest_decrease_date = ""

    for i in range(1, len(rows)):  
        current_profit = float(rows[i][1])
        previous_profit = float(rows[i - 1][1])
        profit_change = current_profit - previous_profit

        if profit_change > highest_increase:
            highest_increase = profit_change
            highest_increase_date = rows[i][0]

        if profit_change < highest_decrease:
             highest_decrease = profit_change
             highest_decrease_date = rows[i][0]

        
    print(f"Greatest Increase in Pofits: {highest_increase_date}  (${highest_increase})")
    print(f"Greatest Decrease in Pofits: {highest_decrease_date}  (${highest_decrease})")

    #create the output and print the results

    with open("analysis/Output.txt", "w") as text_file:
        text_file.write("Financial Analysis\n")
        text_file.write("----------------------------\n")
        text_file.write(f"Total Months: {month_count}\n")
        text_file.write(f"Total: ${net}\n")
        text_file.write(f"Average Change: ${average_change}\n")
        text_file.write(f"Greatest Increase in Pofits: {highest_increase_date}  (${highest_increase})\n")
        text_file.write(f"Greatest Decrease in Pofits: {highest_decrease_date}  (${highest_decrease})\n") 







    

    





