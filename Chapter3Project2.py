#Chapter3 Project 1
#ask for users tp input a primary color.
color1 = input('Enter primary color:')
color2 = input('Enter primary color:')

#if user input is a primary color excute mixing display.
#else display "You didnt input two primary colors".
if (color1 == 'yellow' or color1 == 'red'or color1== 'blue') \
   and (color2 == 'yellow' or color2 == 'red'or color2 == 'blue'):
    
    # assgin the mixed color to newColor with respeect to users input.
    # red and blue make purple.
    if (color1 == 'red' or color2 == 'red') \
       and (color1  == 'blue' or color2 == 'blue'):
        newColor = 'purple'
    #red and yellow make orange.
    elif  (color1 == 'red' or color2 == 'red') \
       and (color1  == 'yellow' or color2 == 'yellow'):
        newColor = 'orange'
    # blue and yellow make green.
    elif  (color1 == 'blue' or color2 == 'blue') \
       and (color1  == 'yellow' or color2 == 'yellow'):
        newColor = 'green'
    
    #display user the mixed color.    
    print(f'When you mix {color1} and {color2}, you get {newColor}.')
else:
    #display user had an inncorrect input.
    print("You didn't input two primary colors.")
