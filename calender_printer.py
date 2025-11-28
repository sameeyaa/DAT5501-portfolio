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

#Run the calendar printer
calendar_printer()

#printer successfully runs

#create a GUI
root = tk.Tk()
root.title("Calender Printer")
root.geometry("600x400")

title_label = tk.Label(root, text = "Calender Printer", font = ("Calibri, 14"))
title_label.pack(pady = 10)

frame = tk.Frame(root)
frame.pack()

#ask for the number of days
tk.Label(frame, text = "Days on Month:").grid(row = 0, column = 0, sticky = "w")
days_entry = tk.Entry(frame, width = 10)
days_entry.grid(row = 0, column = 1)

#ask for the start day of the month
tk.Label(frame, text = "Enter Start Day (0 = Sunday .... 6 = Saturday)").grid(row = 1, column = 0, sticky = "w")
start_day_input = tk.Entry(frame, width = 10)
start_day_input.grid(row = 1, column = 1)

#create buttons to press options
create_button = tk.Button(root, text = "Create Calender", command = calendar_printer)
create_button.pack(pady = 10)

#calender display
output_label = tk.Label(root, text = "", font = ("Calibri", 12), justify = "left")
output_label.pack()

root.mainloop()

