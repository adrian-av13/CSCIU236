#cups of ingrendents for 48 cookies.
sugar, butter, flour = 1.5, 1, 2.75

#orginial count of cookies for the recipe.
ogQuantity = 48

#ask user for amount of wanted cookies.
cookieCount = float(input('Enter number of cookies:'))

#Calculation for the needed amount of sugar, butter, and flour.
sugar = (cookieCount / 48) * sugar
butter = (cookieCount / 48) * butter 
flour = (cookieCount / 48) * flour

print(f'You need {sugar} cups of sugar, {butter} cups of butter, and {flour} cups of flour.')
