# CSCIU236- PythonProject - Adrian Alamilla-Vega 04/14/24 
# Program is a statistics calculator used to help find the average, variance, standard variation, and Standard error(mean +/- standard deviation) of a given sample.
# User can calculate a single sample and are given the choice to compare a second sample to find difference of value and if they're signifcantlly different from each other.
def main():
    # create the 'repeat' variable that will be controlled by user. 
    repeat = 'y'
    
    # Exception handler to prevent input errors by the user.  
    try:
        # while loop that loops with the condition if the 'repeat' variable is 'y,' the users input for yes.
        # created inorder for user to continue calculte their desiered inputs. 
        while repeat == 'y':
            # Within loop creates the two list with Sample class and comapares both.
            
            # Next two lines ask the user for the first sample's name and size of sample.
            # assigned to 'sampleName1' for name and 'Samplesize1' for sample size.
            sampleName1 = input("What is your sample's name?\n")
            sampleSize1 = int(input(f'How many indivduals are in {sampleName1} sample?\n'))
            
            # Creates variable 'sampleList1' that is the list containing the data of each individual in sample.
            # The variable is assigned to a object created by the Sample class with the name and size of sample as parameters.
            # Then calls for the 'create' method in Sample class that creates a list for user to input data. 
            sampleList1 = Sample(sampleName1, sampleSize1).create()

            # Creates the 'avg1' variable that is assigned to the average value of the sample data.
            # 'avg1' is assigned to a function call to the 'mean' function with the sample data from sampleList1 as parameter.
            avg1 = mean(sampleList1)
            
            # Creates the 'var1' variable that is assigned to variance value of the sample data.
            # 'var1' is assigned to a function call to the 'varience' function with the sample data from sampleList1 as parameter.
            var1 = variance(sampleList1)
            
            # Creates the 'sd1' variable that is assigned to the standard deviation value of the sample data.
            # 'sd1' is assigned to the operation of 'var1' value to be raised to the exponent of 1/2, or square root of varience.
            sd1 = var1**.5
            
            # new two lines calulate the mean +/- standard error calculated by subtracting/adding half of SD with the average.   
            posSE1 = (sd1/2) + avg1
            negSE1 = avg1 - (sd1/2)
            # Print all output values to user's console.
            print(f'\nCalculations of {sampleName1}:')
            print(f'	Average: {avg1:.2f}')
            print(f'	Variance: {var1:.2f}')
            print(f'	Standard deviation: {sd1:.2f}')
            print(f'	Postive standrad error: {posSE1:.2f}')
            print(f'	Negative standrad error: {negSE1:.2f}\n')
            
            # Creates the 'secondSample' variable that asks if user would like to to compare another sample with first sample.
            secondSample = input('Would you like to compare another sample?\n Enter y for Yes or n for No.\n')
            
            # The if-else condition depends on the 'secondSample,' the if block is excuted if user sets secondSample to 'y.' 
            # if 'secondSample' is 'y' the user will be asked to input the second sample's information.
            # if else the user will be asked if they want to input another sample's information apart from the first input.
            if secondSample == 'y':
                # The user is asked for the second sample's name and assigns it to 'sampleName2'.
                sampleName2 = input("What is your sample's name?\n")
                # The user is asked for the amount of indivduals in the second sample and assigns it to 'sampleSize2'. 
                sampleSize2 = int(input(f'How many indivduals are in {sampleName2} sample?\n'))
                # An object is created with the sample class and called the create method within the class.
                # Using the sample name and size variables as parameters.
                sampleList2 = Sample(sampleName2, sampleSize2).create()
                # Creates the 'avg2' variable that is assigned to the average value of the sample data.
                # 'avg2' is assigned to a function call to the 'mean' function with the sample data from sampleList2 as parameter.
                avg2 = mean(sampleList2)
                # Creates the 'var2' variable that is assigned to variance value of the sample data.
                # 'var2' is assigned to a function call to the 'varience' function with the sample data from sampleList2 as parameter.
                var2 = variance(sampleList2)
                # Creates the 'sd2' variable that is assigned to the standard deviation value of the sample data.
                # 'sd2' is assigned to the operation of 'var2' value to be raised to the exponent of 1/2, or square root of varience.
                sd2 = var2**.5
                posSE2 = (sd2/2) + avg2
                negSE2 = avg2 - (sd2/2)
                # print the calculated values as an output to console.
                print(f'\nCalculations of {sampleName2}:')
                print(f'	Average: {avg2:.2f}')
                print(f'	Variance: {var2:.2f}')
                print(f'	Standard deviation: {sd2:.2f}')
                print(f'	Postive standrad error: {posSE2:.2f}')
                print(f'	Negative standrad error: {negSE2:.2f}\n')
                avgDif = avg1 - avg2
                varDif = var1 - var2
                sdDif = sd1 - sd2
                print(f'The difference between {sampleName1} and {sampleName2}:')
                print(f'	The difference in average is: {avgDif:.2f}')
                print(f'	The difference in variance is: {varDif:.2f}')
                print(f'	The difference in standard deviation is: {sdDif:.2f}\n')
                
                if((posSE1<negSE2)or(negSE1>posSE2)):
                    print(f'There is a significant difference betwenn {sampleName1} and {sampleName2}.\n')
                else:
                    print(f'There is no significant difference betwenn {sampleName1} and {sampleName2}.\n')
                # Ask user if they would like to calculate a new samples information, seperate from the first two calculations.
                # the input is assigend to the 'repeat' variable that controls the condition of the while loop.
                # the while loop will continue if input is 'y' or stop with any other input.
                repeat = input('Would you like to calculate another sample?\n Enter y for Yes or n for no\n')
            else:
                # if user doesn't want to compare another sample to the first, they are asked if they'd like to calculate information for a new sample.
                # the input is assigend to the 'repeat' variable that controls the condition of the while loop.
                repeat = input('Would you like to calculate another sample?\n Enter y for Yes or n for no\n')
    except:
        # if exception occurs program stoped and outputs to user to input valid number.
        # used incase it user input invalid numbers.
        print('Please enter valid value.')
        
# defines the 'varience' function with the parameter of sample data as a list.    
def variance(sampleList):
    # creates 'av' that conatins the average value of the sample's data.
    # that is assigned to a call to the 'mean' function and uses the parameter of the 'varience' function as the parameter.
    av = mean(sampleList)
    # The for loop calculates the ssd or sum standarad deviation.
    # loop interates for each element in the sample list parameter.   
    for i in range(len(sampleList)):
        # Each element conatins the data inputed for indivdual in sample and is subtracted by the average of the entire sample.
        sampleList[i] = sampleList[i] - av
        # Each element in list paramter is raised to the second power. 
        sampleList[i] = sampleList[i]**2
    # creates 'ssd' variable, sum standard deviation, that is assigned to the sum of the entire list after calculations were made.
    ssd = sum(sampleList)
    # creates 'varience' variable that is assigned to the operation of the 'ssd' varible divided by the length of the list parament minus one. 
    variance = ssd / (len(sampleList)-1)
    # finally returns that 'varience' variable that conatains the varience value of the sample list parameter.
    return variance

# defines the 'mean' function that accpets the list containg the sample's data as paramter.  
def mean(sampleList):
    # the 'total' variable is createsd and assigned to the sum of the provided parameter, the total value of all indivdual's data in the sample.
    total = sum(sampleList)
    # the 'average' variable is created and assigned to an operation of the 'total' variable divided by the amount of indudivals in the sample.
    average = total/(len(sampleList))
    # returns the 'average' variable containg the calculated average of the provided sample. 
    return average

# creates class called 'Sample' that will create the user's samples as an object.
class Sample():
    # intializes the samples attributes which are the name and size of the sample.
    # Allowing the class to accept name and size as parameters.
    def __init__(self, name, size):
        self.__name = name
        self.__size = size
    # method that allows to create a sample into list.
    def create(self):
        # creates empty list that is assigned to the variable 'sampleList'
        sampleList = list()
        # A for-loop that interates in respect to the amount of indivduals in the sample.
        # Within the loop it allows user to input each indivdual's collected data and add to a list.
        for i in range(self.__size):
            # Asks to input the value of a special indivudal in sample. 
            # Creates 'indivData' variable is is assigned to the user's input value for the indivdual. 
            indivData = float(input(f'Enter data recorded for individual #{i+1}: '))
            # adds 'indivData' the user's inputed data for indivdual to the 'sampleList' the list.
            sampleList.append(indivData)
        # returns the 'sampleList' a list that conatins each indivduals collected data.
        return sampleList
    
    

if __name__ == '__main__':
    main()
