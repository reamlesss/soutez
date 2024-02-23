def generatePyramid(char,rowCount):
    
    #check if user entered valid rowCount value
    if rowCount <= 0 or not char.strip():
        print("Please enter valid rowCount value.")
        return

    for i in range(rows):
        row = ''
        #count the number of spaces at the beginning of row
        spaces = rows - i - 1
        #add needed count of spaces
        for j in range(spaces):
            row += ' '
        #add characters to the row
        for k in range(2 * i + 1):
            row += char

        print(row)    

#getting data from user
char = input("Please enter character to use in pyramid generation: ")
rows = input("Please enter row count to use in pyramid generation: ")

try:
    rows = int(rows)
except ValueError:
    print("Rowcount needs to be a number")
    exit()
#call the function generatePyramid
generatePyramid(char,rows)
  