#list ch 7
#nameInput = input('Enter a name: ')
#nameLst = []
#with open('popular_names.txt', 'r') as names:
#    name = names.readline()
#    while name != '':
#        name = name.rstrip('\n')
#        nameLst.append(name)
#        name = names.readline()
#    if nameInput in nameLst:
#        print('That was a popular name between 2000 and 2009.')
#    else:
#        print('That was not a popular name between 2000 and 2009.')
magic_sqr = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
def is_magic_square(x):
    row = 3
    firstCSum = 0
    secondCSum = 0
    thirdCSum = 0
    fstDiagSum = 0
    scdDiagSum = 0
    # find diagonial sum forward.
    scdDiagSum = x[1][1] + x[0][2] + x[2][0]
    # find column sums and backward diagonial sum.
    for r in range(row):
        fstDiagSum += x[r][r]
        firstCSum += x[r][0]
        secondCSum += x[r][1]
        thirdCSum += x[r][2]
    #verify all sums and return respected value.
    if sum(x[0]) == sum(x[1]) == sum(x[2]) == firstCSum == secondCSum == thirdCSum == scdDiagSum == fstDiagSum:
        return True
    else:
        return False

print(is_magic_square(magic_sqr))

