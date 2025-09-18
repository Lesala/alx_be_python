# promptingthe user to enter the pattern size number
size = int(input("Enter the size of the pattern: "))
# initializing the row variable
row = 0
# Generating the pattern using nested loops
while row < size:
    row += 1
    # Using for loop for columns
    for col in range (size):
        print("*", end ="")
    print()  # Move to the next line after each row