#ask user for number of males and females.
males = int(input('Enter number of males:'))
females = int(input('Enter number of females:'))

#calculate percentage of males and females.
pMales = ((males / (males + females))* 100)
pFemales = ((females / (males + females))*100)

#output
print(f"""Percent males: {pMales:.0f}%
Percent females: {pFemales:.0f}%""")