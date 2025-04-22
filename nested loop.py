

rows = int(input("Enter the  number of rows : "))
columns = int(input("Enter the  number of columns : "))
symbol = input("Enter a symbol to use : ")

for x in range(rows):
   for counter in range(columns):
    print(symbol, end="")
   print()


