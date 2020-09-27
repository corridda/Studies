year = 2000
month = 10
day = 24
hour = 11
minute = 33
second = 15

def valid():
    if 1900 < year < 2100 and 1 <= month <= 12 \
       and 1 <= day <= 31 and 0 <= hour < 24 \
       and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
            return 1

print(valid())