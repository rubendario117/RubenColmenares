import csv
import sys

csvpath ="C:/Users/Ruben D. Colmenares/Documents/TEC/Data Bootcamp/Github Repository/RubenColmenares/python-challenge/PyBank/budget_data.csv"

with open (csvpath, newline='') as main:

    csvfile = csv.reader(main, delimiter=',')

    csv_header = next(csvfile)

    #Count Months and SUM Profit/Losses
    months=[]
    values=[]
    total = 0
    avg = 0

    for x in csvfile:
        months.append(str(x[0]))
        values.append(float(x[1]))
        total = total + int(x[1])

    #Unique values on "Months":
    unique_months = set(months)
    #Average:
    avg = total / len(months)
    #float(avg)
    
    #Find Max and Min index in order to get their Months:
    maxpos = values.index(max(values)) + 1
    minpos = values.index(min(values)) + 1
    #print ("maxpos= " + str(maxpos))

print("Financial Analysis: \n")
print("--------------------------- \n")
print("Total Months: " + str(len(unique_months)))
print("Total: $" + str(total))
print("Average Change: $" + str(avg))
print("Greatest increase in Profits: " + str(months[maxpos]) + " ($" + str(max(values)) + ")") #Using the Max function
print("Lowest increase in Profits: " + str(months[minpos]) + " ($" + str(min(values)) + ")") #Using the Min function

#Redirect Print to .txt
sys.stdout=open("main_output.txt","w")
print("Financial Analysis: \n")
print("--------------------------- \n")
print("Total Months: " + str(len(unique_months)))
print("Total: $" + str(total))
print("Average Change: $" + str(avg))
print("Greatest increase in Profits: " + str(months[maxpos]) + " ($" + str(max(values)) + ")") #Using the Max function
print("Lowest increase in Profits: " + str(months[minpos]) + " ($" + str(min(values)) + ")") #Using the Min function
sys.stdout.close()