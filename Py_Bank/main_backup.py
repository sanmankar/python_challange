import os
import csv

# Define function to count year and months

def sub_calc(val):

    # Initialize variables...
    cnt = 1
    cnt_yr = 1
    net_amount = 0
    avg_amount = 0
    grtst_increase = 0
    grtst_decrease = 0
    prior_val_incr = 0
    prior_val_dcrs = 0
    msg = []

    for row in val:

        net_amount = net_amount + int(row[1])

        if cnt == 1 :
            yr = row[0]
            grtst_increase = int(row[1])
            grtst_decrease = int(row[1])
            cnt = 99
            # print(yr)

        if yr != row[0]:
            cnt_yr = cnt_yr + 1
            yr = row[0]
            # print(f'Yr : {yr} Count Year: {cnt_yr}')

        if int(grtst_increase) < int(row[1]):
            grtst_increase = int(row[1])
            grst_chg_incr = int(row[1]) - int(prior_val_incr)
            grtst_incr_yr = row[0]
        else:
            prior_val_incr = int(row[1])
        
        if int(grtst_decrease) > int(row[1]):
            grtst_decrease = int(row[1])
            grst_chg_dcrs = int(row[1]) - int(prior_val_dcrs)
            grtst_dcrs_yr = row[0]
        else:
            prior_val_dcrs = int(row[1])
        
    # End of For Loop

    avg_amount = float(net_amount/cnt_yr)

    # Create the ouptput in an array
    msg.append(f'Total Months: {cnt_yr}')
    msg.append(f'Total: {net_amount}')
    msg.append(f'Average Change: {avg_amount}')
    msg.append(f'Greatest Increase in Profit: {grst_chg_incr} during {grtst_incr_yr}')
    msg.append(f'Greatest Decrease in Profit: {grst_chg_dcrs} during {grtst_dcrs_yr}')
    return msg

'''
    ******* Main part of the script *******
'''

# Read the CSV file

_=os.system("clear")
budgetCSV = os.path.join(".","Data","budget_data.csv")

with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f'Header: {csv_header}')

    # x = sub_calc(csvreader)

    for x in sub_calc(csvreader):
        print(x)

 