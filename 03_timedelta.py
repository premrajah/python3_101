#
# Comments go here
#
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    # construct a basic timedelta and print it
    print(timedelta(days=365, hours=5, minutes=1))

    # print todays date
    now = datetime.now()
    print("Today is: ", str(now))

    # todays date 1 year from now
    print("1 year from now: ", str(now + timedelta(days=365)))

    # create a timedelta that uses more than one argument
    print("In 2 days and three weeks it will be: ", str(now + timedelta(days=2, weeks=3)))

    # calculate the date 1 week ago, formatted as a string
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d %Y")
    print("1 week ago it was: ", s)

    print("-----")

    # How anys days until next aprils fool day
    today = date.today()
    afd = date(today.year, 4, 1)

    # use date comparison to see if april fool's has already gone for this year
    # if it has, use the replace() function to get the date next year
    if(afd  < today):
        print("Aprils fools day already went by %d days ago" % ((today-afd).days))
        afd = afd.replace(year = today.year+1)

    # now calculate the amount of time until Aprils fools's day
    time_to_afd = afd - today
    print("It's just", time_to_afd, " days unitl April fool's day")



if __name__ == "__main__":
    main()