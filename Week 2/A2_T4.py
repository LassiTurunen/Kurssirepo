#A2_T4: Average and rounding

#Prompt the user to insert the minutes spent on each previous topic task. Calculate the sum and the average. 
# Display those in the example program run format(Note! precision). 
# Make sure to calculate the required average for two decimal digits and later integer as rounded integer (precision 0 + type conversion).

print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

Task_1 = int(input("#A1_T1: "))
Task_2 = int(input("#A1_T2: "))
Task_3 = int(input("#A1_T3: "))
Task_4 = int(input("#A1_T4: "))
Task_5 = int(input("#A1_T5: "))
Task_6 = int(input("#A1_T6: "))
Task_7 = int(input("#A1_T7: "))

Total = Task_1 + Task_2 + Task_3 + Task_4 + Task_5 + Task_6 + Task_7
Average = float(Total / 7)

print(f"\nIn total you spent {Total} minutes on programming.")

print(f"Average per task was {round(Average,2)} min and same rounded to the nearest integer {round(Average)} min.")

print("\nProgram ending.")

    #Example program run:

#Program starting.
#Estimate how many minutes you spent on programming...

#A1_T1: 3
#A1_T2: 7
#A1_T3: 9
#A1_T4: 8
#A1_T5: 13
#A1_T6: 14
#A1_T7: 21

#In total you spent 75 minutes on programming.
#Average per task was 10.71 min and same rounded to the nearest integer 11 min.

#Program ending.