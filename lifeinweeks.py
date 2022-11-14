# Tip Calculator
from calendar import day_name, month, monthcalendar, week
from datetime import date


# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
totalage = 90 - age

daycal = 365 * totalage
weekcal = 52 * totalage
monthcal = 12 * totalage

print(f'You have {daycal} days, {weekcal} weeks, and {monthcal} months left in life')
