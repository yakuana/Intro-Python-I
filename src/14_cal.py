"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - [x] If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - [x] If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - [x] If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

def makeCalendar(date):

  # yr = current year
  # mon = current month
  # day = current day 
  yr, mon, day = str(datetime.now()).split(' ')[0].split('-')
  
  if (len(date.split()) > 1):   
    # user gave two inputs 
    print(calendar.month(int(date.split()[1]), int(date.split()[0])))

  elif (date):
    # user gave one input 
    print(calendar.month(int(yr), int(date)))

  else: 
    # user did not give an input 
    print(calendar.month(int(yr), int(mon)))

print("Calendar Printer: For any month of any year!")

date = input("Enter the month (1-12) and the year (optional): ")
print("")

makeCalendar(date)
