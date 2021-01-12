#Part I - Create script to import data from CSV file
#Set modules for importing the data
import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Define lists and variables to store data
row_count = 0
canidate = ["Khan", "Correy", "Li", "O'Tooley"]

khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

kpercent = 0
cpercent = 0
lpercent = 0
opercent = 0



print("Election Results")
print("-------------------------")

#Part II - Loop through the data set to print the calculations
# open csv file path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
      
    # Read each row of data after the header
    csv_header = next(csvreader)       

    for row in csvreader:

        #Calculate the total number of individual votes and add to row_count list
        row_count = sum(1 for row in csvreader) 
        
        #Capture the canidate list
        #Calculate the total of votes each canidate won

        khan_count = 
        correy_count =
        li_count =
        otooley_count = 
    
       

        #Calculate the percentage of votes each candidate won
        kpercent = (khan_count)/(row_count)
        kpercent =str(round(kpercent,2))

        cpercent = (correy_count)/(row_count)
        cpercent =str(round(cpercent,2))

        lpercent = (li_count)/(row_count)
        lpercent =str(round(cpercent,2))

        opercent = (otooley_count)/(row_count)
        opercent =str(round(cpercent,2))


        #Create a dictionary which holds all election results
       
       election_results = {[canidate:"Khan", percent:"kperent", vote: "khan_count"],
                            [canidate:"Correy", percent:"cperent", vote: "correy_count"],
                            [canidate:"Li", percent:"lperent", vote: "li_count"],
                            [canidate:"O'Tooley", percent:"operent", vote: "otooley_count"]}

        print(election_results)


        #The winner of the election based on popular vote
        #Create conditional to determine election results


    
    ###Other Attempts for part 2--------------------------------------------------
    #     if str(row[2]) == Khan:
    #         Khan_Vote.append(khan)
    # print(Khan_Vote)

    #option 4
     # khan_vote = khan_vote + int(row[2])
        # khan_count = int(row[2]) - previous
        # khan_total.append(khan_count)
        # previous = int(row[2])

    #option 5
        #Create a list which will store canidate names
        #  if canidate == Khanint([2]:
        #     khan_count = Khan + 1
            
        # if canidate == Correy[2]:
        #     correy_count == Correy + 1

        # if canidate == Li[2]:
        #     li_count = Li + 1

        # if canidate == OTooley[2]:
        #     otooley_count = "O'Tooley" + 1             
            

            # canidate_list.append(canidate)
            # previous = int(row[2])   
        
        # #option 3
        # if canidate not in canidate_list:
        #     canidate_list.append(canidate)
        #     previous = str(row[2])
        
        # #Option 2
        # canidate = canidate + str(row[2])
        # canidate_count = str(row[2]) - previous
        # canidate_list.append(canidate_count)
        # previous = str(row[2])
        
        
        # #Option 1
        # #if (row[2]) not in canidate_list:
        #     #canidate_list.append(row[2])
        #     # #previous = row[2]
        
#Print all analysis on Election Results
print(f'Total Votes: {1 + row_count}')
print("-------------------------")
print(election_results)


#Specify the file export the Financial Data to write as txt file)
# Set variable for output file
#output_file = os.path.join('..', 'Pypoll', 'Analysis',"Election_Results.csv")

# Open the output file
# with open(output_file, "w", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Election Results"])
#     writer.writerow(["Total Votes: "])
#     writer.writerow([""])
#     writer.writerow([""])
#     writer.writerow([""])
#     writer.writerow([""])
   