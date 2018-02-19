#
# Comments go here
#
import calendar

def main():
    # plain text calender
    c = calendar.TextCalendar(calendar.SUNDAY)
    st = c.formatmonth(2018, 1, 0, 0)
    print(st)

    print("---")

    # create a HTML formatted calandar
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    hca = hc.formatmonth(2018, 1)
    print(hca)

    print("---")

    # loop over the days of a month
    # zeroes mean that the day of the week is an overlapping month
    for i in c.itermonthdays(2018, 8):
        print(i)

    print("---")

    # calender module provides usefull utilities for the given local
    # sucha s names of days and months in both full and abbreveated forms
    for name in calendar.month_name:
        print(name)

    print("---")

    for day in calendar.day_name:
        print(day)

    print("---")

    # calculate days based on a rule: 
    # example: first friday of every month
    print("-- First friday of every month --")
    print("Team meeting s will be on: ")
    for m in range(1, 13):
        cal = calendar.monthcalendar(2018, m)
        weekone = cal[0]
        weektwo = cal[1]

        if(weekone[calendar.FRIDAY] != 0):
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[m], meetday))
        
         

if __name__ == "__main__":
    main()