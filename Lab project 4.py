#inital cost of tuition
#cost = 8000
#the first year increase calculation and displays its cost.
#cost = cost * 1.03
#print(f'In 1 year, the tutition will be ${cost}.')
# increase in cost from years 2 to 5 calculations and displays the costs.
#for year in range(2, 6):
#    cost = cost * 1.03
#    print(f'In {year} years, the tutition will be ${cost}.')

#ask user for nonegative number and intialize total.
number = int(input('Enter a nonnegative integer:'))
total = 1
#preform calucation with rescpect to input with a loop.
for i in range (1, number + 1):
    total *= i
#print calculation.
print(total)