#Duration Calender that can: take a date input from user and calculate how many days until today
 
#import datetime function to input dates
import datetime
from datetime import datetime, date

#date.today will mean the code will always be updated to use the present day it is being ran on
today = date.today()
print("Today's date:", today) #the date is formatted year-month-day (YYYY-MM-DD)

#ask user to input the second date that they want to calculate the difference against
input_str = input("Please enter the date you want to calculate from in the format (YYYY-MM-DD): ")
date2 = datetime.strptime(input_str, "%Y-%m-%d").date()  
#parse the string to format as a date

#calculate the difference between the inputted date and today
difference = (today - date2)
print(difference)
