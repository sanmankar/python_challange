import os
import csv

# Define function to count year and months

def sub_calc(val):

    # Initialize variables...
    cnt = 1
    cnt_yr = 1
    net_amount = 0
    tot_change = 0
    avg_change_prnt = 0
    grtst_increase = 0
    grtst_decrease = 0
    prior_val = 0
    curr_val = 0
    msg = []

    for row in val:

        net_amount = net_amount + int(row[1])

        if cnt == 1 :
            yr = row[0]
            grtst_increase = int(row[1])
            grtst_decrease = int(row[1])
            cnt = 99
            print(yr)

        if yr != row[0]:
            cnt_yr = cnt_yr + 1
            yr = row[0]
            # print(f'Yr : {yr} Count Year: {cnt_yr}')
        
        # Assigning Current value
        curr_val = int(row[1])

        if  grtst_increase < curr_val:
            grtst_increase = curr_val
            grst_chg_incr = curr_val - prior_val
            grtst_incr_yr = row[0]
        elif grtst_decrease > curr_val:
            grtst_decrease = curr_val
            grst_chg_dcrs = curr_val - prior_val
            grtst_dcrs_yr = row[0]


        # Calvulate net_change
        if row[0] != "Jan-2010" : 
            tot_change = tot_change + (curr_val - prior_val)
        
       
        # Assigning prior value

        prior_val = curr_val
     
        
    # End of For Loop

    avg_change_prnt = float(tot_change/cnt_yr-1)

    # Formatting values for printing
    net_amount_str = '${:,.2f}'.format(net_amount)
    avg_change_prnt_str = '${:,.2f}'.format(avg_change_prnt)
    grst_chg_incr_str = '${:,.2f}'.format(grst_chg_incr)
    grst_chg_dcrs_str = '${:,.2f}'.format(grst_chg_dcrs)

    # Create the ouptput in an array

    msg.append(f'Total Months: {cnt_yr}')
    msg.append(f'Total: {net_amount_str}')
    msg.append(f'Average Change: {avg_change_prnt_str}')
    msg.append(f'Greatest Increase in Profit: {grst_chg_incr_str} during {grtst_incr_yr}')
    msg.append(f'Greatest Decrease in Profit: {grst_chg_dcrs_str} during {grtst_dcrs_yr}')
    return msg

## End of function sub_calc()


'''
    ***************************************
    *                                     *
    ******* Main part of the script *******
    *                                     *
    ***************************************
'''


# This command clears the standard output (screen)
_=os.system("clear")

# Read the CSV file
budgetCSV = os.path.join(".","Data","budget_data.csv")

# Create another file handler for writing the results
budgetanlyTXT = os.path.join(".","Data","buget_analysis.dat")

with open(budgetanlyTXT,'w') as txtfile:
    txtfile.write("Output of the Analytis is : \n")
    txtfile.write ("--------------------------- \n")

with open(budgetCSV, 'r') as csvfile:
    with open(budgetanlyTXT,'a') as txtfile:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        print(f'Header: {csv_header}')

        for x in sub_calc(csvreader):
            print(x)
            txtfile.write(x)
            txtfile.write("\n")

# Close file handles for both input and output files
csvfile.close()
txtfile.close()

