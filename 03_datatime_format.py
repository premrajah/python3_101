#
# Comments go here
#
from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string 
    # control codes

    ## DATETIME formatting
    now = datetime.now()

    # %y%Y - Year
    # %a%A - Weekday
    # %b%B - Month
    # %d - Daay of Month
    print(now.strftime("%a | %d | %B | %y"))

    # %c - Locale date and time
    # %x - Locale date
    # %X - Locale time
    print(now.strftime("Locale Data and time: %c"))
    print(now.strftime("Locale Data : %x"))
    print(now.strftime("Locale time: %X"))

    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24Hour time: %H:%M"))

if __name__ == "__main__":
    main()