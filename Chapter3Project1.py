# chapter 3 project 1 
# ask user for month, day, and year.
month = int(input('Enter month (numeric):'))
day = int(input('Enter day:'))
year = int(input('Enter two digit year:'))

# calculate magic year with given.
magicYear = day * month

# if given year is the same as magic year dislay "This date is magic"
# else display "this date is not magic."

if year == magicYear:
    print('This date is magic!')
else:
    print('This date is not magic.')