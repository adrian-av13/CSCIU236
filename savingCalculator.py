#ch 5 lab savings amount over inputed months
#main function that prints calculation function for user input. 
def main():
    print(future_value(present_value(), interest_rate(), months()))
    
#Calculation of future balance after inputed months
def future_value(present_value, interest_rate, months):
    total = present_value * (1 + interest_rate) ** months
    return total

#ask user to input current savings balance.
def present_value():
    balance = float(input('Enter current bank balance:'))
    return balance

#Ask user to input intreset rate.
def interest_rate():
    rate = float(input('Enter interest rate:'))
    return rate

#Ask user for the amount of months later.
def months():
    num_months = int(input('Enter the amount of time that passes:'))
    return num_months

#call main function.
main()