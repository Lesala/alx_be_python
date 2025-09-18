# Prompting the userto enter a number to generate its multiplication table
number = int(input("Enter a number to see its multiplication table: ")) 
# Generating the multiplication table for the entered number
for i in range(1,11):
    print(f'{number} * {i} = {number * i}')
