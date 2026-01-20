# Q.1) Write a Python program which accepts the user's first and last name and print them in  
# reverse order with a space between them.    

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"{last_name} {first_name}")

# Q.2) Write a Python program to print the calendar of a given month and year.  
# Note : Use 'calendar' module.   
import calendar
year = int(input("Enter year (e.g., 2023): "))
month = int(input("Enter month (1-12): "))
print(calendar.month(year, month))
# Q.3)  Write a Python program to calculate number of days between two dates.   
# [ use datetime module ] 
# Sample dates : (2014, 7, 2), (2014, 7, 11)   
# Expected output : 9 days   
from datetime import datetime

# Q.4)  Write a Python program to test whether a passed letter is a vowel or not. 