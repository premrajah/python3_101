#
# Reading and writing files
#

def main():
    ## Open a file for writing and create it if it does not exist
    # f = open("textfile.txt", "w+")

    ## open file for appending text to the end
    ## a = append 
    # f = open("textfile.txt", "a")

    ## read file
    f = open("textfile.txt", "r")

    if f.mode == 'r':
        ## contents = f.read()
        fl = f.readlines()
        for x in fl:
            print(x)

    ## write some lines of data
    # for i in range(10):
    #     f.write("This is a line" + str(i) + "\r\n")

    
    ## close the file when done
    # f.close()

    print("...done.")




if __name__ == "__main__":
    main()