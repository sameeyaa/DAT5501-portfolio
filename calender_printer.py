#Calendar Printer
#implementing tkinter to advance my code 

import tkinter as tk
from tkinter import ttk

def calendar_printer():
    # Input function to enter number of days in the month
    days_in_month = int(input("How many days are in the month? "))

    # Input function to enter what day the first of the month falls on
    day_month_starts = int(input("What day does the month start on? (0=Sunday, 1=Monday, ..., 6=Saturday): "))

    #Header with the days of the weeks for numbers to fall under
    print("S  M  T  W  T  F  S")
    
    #Ensure a new line starts from Sunday and after every 7 days
    counter = 0


    #Create blank spaces to the dates map out nicely and fall under each day in the header and are not joined together
    calendar_text += "   " * day_month_starts
    counter += day_month_starts
    for _ in range(day_month_starts):
        print("   ", end="")
        counter += 1

    #Print under all the days of the week
    for day in range(1, days_in_month + 1):
        print(f"{day:>2} ", end="")  
        counter += 1

        #After printing 7 days,a new line will be made
        if counter == 7:
            print()
            counter = 0

    print()  

    output_label.config(text = calender_text)

#Run the calendar printer
#calendar_printer()

#printer successfully runs


