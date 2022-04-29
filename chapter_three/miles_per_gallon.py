gallon_used = 0
total_gallon_used = 0
total_miles_covered = 0
while gallon_used != -1:
    gallon_used = int(input('Enter Gallon Used or -1 to end: '))
    total_gallon_used += gallon_used
    miles_covered = int(input('Enter Miles Covered or -1 to end: '))
    total_miles_covered += miles_covered
average_miles = total_miles_covered / total_gallon_used
print(f'the total miles covered is {total_miles_covered}\n the gallons used is {total_gallon_used}\n the average '
      f'miles covered per gallon is {average_miles}')
