import os
import csv

'''
    ***************************************
    *                                     *
    ******* Main part of the script *******
    *                                     *
    ***************************************
'''


# This command clears the standard output (screen)
_=os.system("clear")
 
#voter_dict = {'Candidate': " ",'County' : " ",'VoterID': " "}
votes = {}
max_votes=0
msg=[]
print_msg= ""
winner=""

# Read the CSV file
electionCSV = os.path.join(".","Data","election_data.csv")

# Create another file handler for writing the results
electionanlyTXT = os.path.join(".","Data","election_analysis.dat")

with open(electionanlyTXT,'w') as txtfile:
    txtfile.write("    Election Results: \n")
    txtfile.write ("--------------------------- \n")

with open(electionCSV, 'r') as csvfile:


        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        #print(f'Header: {csv_header}')

        candidate = " "
        cnt_votes = 1
        cnt = 1


        for row in csvreader:


            candidate = row[2]

            if cnt == 1 :
                vote_id = row[0]
                cnt = 99


            if vote_id != row[0]:
                cnt_votes = cnt_votes + 1
                vote_id = row[0]

            if  candidate in votes:
                candidate = row[2]
                votes[candidate] = votes[candidate] + 1
            else:
                votes[candidate] = 1

        
        msg.append(f'------------------------')
        msg.append(f'Total Votes: {cnt_votes})')
        msg.append(f'------------------------')
    
        for key,value in votes.items():
            if max_votes < value:
               max_votes = value
               winner = key

            pct_votes = '{0:.00%}'.format(value/cnt_votes)
            msg.append(f'{key} : {pct_votes} ({value})')
        
        msg.append(f'------------------------')    
        msg.append(f'     Winner: {winner}')
        msg.append(f'------------------------')

        with open(electionanlyTXT,'w') as txtfile:
            txtfile.write("    Election Results: \n")
            txtfile.write ("--------------------------- \n")
            for print_msg in msg:
                print(print_msg)
                txtfile.write(print_msg)
                txtfile.write("\n")

csvfile.close()
txtfile.close()

