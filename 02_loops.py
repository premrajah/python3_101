#
# loops
#

def main():
    x = 0

    # while loop
    while (x < 5):
        print(x)
        x = x+1

    print("---")

    # define for loop
    for x in range(5, 10):
        print(x)

    print("---")

    # use for loop over collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for d in days:
        print(d)    
    
    
    print("---")

    # use of break and continue
    for x in range(5, 10):
        if(x == 7): break
        print(x)

    print("---")

    for x in range(5, 10):
        if(x % 2 == 0): continue
        print(x)

    print("---")

    # using the enumerate() function to get index
    for i, d in enumerate(days):
        print(i, " - ", d)

        









if __name__ == "__main__":
    main()