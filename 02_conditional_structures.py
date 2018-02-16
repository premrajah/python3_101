#
# Conditionals
#

def main():
    x, y = 100, 10

    # conditionl flow uses if, elif, else 
    if (x < y):
        st = "x is less than y"
    elif (x == y):
        st = "X is equal to y"
    else:
        st = "X is greater than y"
        
        
    print(st)

    print("---")

    # conditional statements "a if C else b" 
    st = "x is less than y" if(x < y) else "x is greater than or the same as y"

    print(st)



if __name__ == "__main__":
    main()