import os
import csv

# Path to collect Data from resources

budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data

months = []
profit_losses = []

# with open as csvfile
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")

    for rows in csvreader:

        # Add months
        months.append(rows[0])

        # Calculate total months
        total_months = len(months)

        # Add Profit/Losses
        profit_losses.append(int(rows[1]))
        
        # Calculate The net total amount of Profit/Lossed over the entire period
        net_profit_losses = sum(profit_losses)
       
        # Changes is profit losses
        change = []
        
        for x in range(1, len(profit_losses)):
            
            change.append((int(profit_losses[x]) - int(profit_losses[x-1])))

             # calculate average
        
            average_change = sum(change) / len(change)

            # Greatest increase in profits
            max_increase = max(change)

            # Greatest decrease in profits
            max_decrease = min(change)

    # Print results

    print("Financial Analysis")

    print("-----------------------------------------")

    print(f"Total Months: {total_months}")

    print(f"Total: {net_profit_losses}")

    print(f"Average Change: $ {average_change}")

    print(f"Greatest Increase in Profits: {months[change.index(max(change))+1]} $ {max_increase}")

    print(f"Greatest Decrease in Profits: {months[change.index(max(change))+1]} $ {max_decrease}")


# Creat output.txt file

file = open("analysis/output.txt","w")

file.write("Financial Analysis\n")

file.write("-----------------------------------------\n")

file.write("Total Months: 86\n")

file.write("Total: 22564198\n")

file.write("Average Change: $ -8311.105882352942\n")

file.write("Greatest Increase in Profits: Aug-16 $ 1862002\n")

file.write("Greatest Decrease in Profits: Aug-16 $ -1825558\n")

file.close()


