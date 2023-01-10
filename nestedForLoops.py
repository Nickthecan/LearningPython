#nested for loop = The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
column = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

#for every row
for i in range(rows):
    #for every column in the row (use j because its standard practice: comes after i)
    for j in range(column):
        #print the symbol (use this format of print to not go to the next line)
        print(symbol, end = "")
    #go to the next line
    print()