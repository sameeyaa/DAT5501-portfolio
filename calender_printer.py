import tkinter as tk
from tkinter import ttk

def calendar_printer():
    try:
        days_in_month = int(days_entry.get())
        day_month_starts = int(start_day_input.get())
    except ValueError:
        output_label.config(text="Please enter valid numbers.")
        return

    #calender contnt
    calendar_text = "S  M  T  W  T  F  S\n"

    counter = 0

    #blank spaces before first day if it doesn't start on a sunday
    calendar_text += "   " * day_month_starts
    counter += day_month_starts

    #add the days of the month
    for day in range(1, days_in_month + 1):
        calendar_text += f"{day:>2} "
        counter += 1

        # New line after 7 days
        if counter == 7:
            calendar_text += "\n"
            counter = 0

    #output to GUI label
    output_label.config(text=calendar_text)


#creating a GUI

root = tk.Tk()
root.title("Calendar Printer")
root.geometry("600x400")

title_label = tk.Label(root, text="Calendar Printer", font=("Calibri", 18))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Days in Month:").grid(row=0, column=0, sticky="w")
days_entry = tk.Entry(frame, width=10)
days_entry.grid(row=0, column=1)

tk.Label(frame, text="Enter Start Day (0 = Sun ... 6 = Sat):").grid(row=1, column=0, sticky="w")
start_day_input = tk.Entry(frame, width=10)
start_day_input.grid(row=1, column=1)

create_button = tk.Button(root, text="Create Calendar", command=calendar_printer)
create_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Courier", 12), justify="left")
output_label.pack()

root.mainloop()
