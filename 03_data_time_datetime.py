#
# data, time, datetime
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
    # DATE OBJECTS
    # get todays date
    today = date.today()
    print("Today's date is ", today)

    # dates individual components
    print("Date components ", today.day, "/", today.month, "/", today.year)

    # today's weekday (0=monday, 6=sunday)
    print("Today's weekdayy number is ", today.weekday())

    days  = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print("Today is - ", days[today.weekday()], " - weekday() array")

    ## DATETIME
    todayTime = datetime.now()

    
    # get todays date from the datetime class
    print("datetime ", todayTime)

    # get current time
    t = datetime.time(datetime.now())
    print(t)



if __name__ == "__main__":
    main()