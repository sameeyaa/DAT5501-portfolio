#Duration Calender that can: take a date input from user and calculate how many days until today
 
#import datetime function to input dates
import datetime
from datetime import date

#ask user to input 2 different dates to work out the difference
d1 = date(2005, 12, 11)
d2 = date(2025, 10, 20)
difference = d2 - d1
print(difference.days)

#however, the difference from today should be worked out, hence the numpy library will need to be imported and datetime.today will need to be used
