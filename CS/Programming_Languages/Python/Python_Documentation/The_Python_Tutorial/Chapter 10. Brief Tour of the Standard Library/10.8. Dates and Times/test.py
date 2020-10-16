# The datetime module supplies classes for manipulating dates and times in both simple and complex ways
from datetime import date
import math

# dates are easily constructed and formatted
now = date.today()
print('now:', now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# # dates support calendar arithmetic
birthday = date(1981, 4, 15)
age = now - birthday
print(f"I'm Igor and I'm {math.trunc(age.days/365)} years old.")
