import datetime

date = int(input("Enter the date on which you were born: "))
month = int(input("Enter the month on which you were born: "))
year = int(input("Enter the year on which you were born: "))

today = datetime.date.today()
current_date = today.day
current_month = today.month
current_year = today.year

date_age = date - current_date
month_age = month - current_month
year_age = current_year - year

print(f"You are {date_age} days {month_age} months and {year_age} years old.")

