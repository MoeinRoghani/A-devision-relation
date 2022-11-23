import math
from decimal import Decimal



def output_2(theta0, iteration):
    output = beta = 0

    for i in range (0 , iteration+1):

        for j in range (i+1, iteration+1):
            beta += math.floor(math.log10(theta0*pow(2,j))+1)
        
        output += theta0*pow(2,i)*pow(10,beta)                            
        beta = 0

    return output


def output_5(theta0, iteration):
    output = beta = 0

    for i in range (0 , iteration+1):

        for j in range (i+1, iteration+1):
            beta += math.floor(math.log10(theta0*pow(5,j))+1)
        
        output += theta0*pow(5,i)*pow(10,beta)                            
        beta = 0

    return output




"""RUN SEction"""

negative = False
theta0 = int(input("Number: "))
if theta0 < 0:
    theta0 = -theta0
    negative = True

choice = int(input("5 or 2 ? "))
while choice != 5 and choice != 2:                                                                     # Choice value should be either 2 or 5
    choice = int(input("5 or 2 ?  (please enter either 2 or 5): "))

iteration = int(input("Iterations: "))
while iteration%2 == 0:                                                                                # number of iterations ahould be an odd number, you can make this if rule as a comment if you want to test with even numbers
    iteration = int(input("Iterations (please enter an odd number): ")) 

output = int( (output_5(theta0, iteration) if choice==5 else output_2(theta0, iteration)) )            # giving the whole number with respect to odd or even function
if negative == True:
    output = -output

print("Result:", output, '\n', "= 3 * %s and division remainder = %f" %(Decimal(output)/3,output%3))    # for having the exact deciaml values after decimal point i changed the output type to Decimal, and because it was big to be a float type when deviding by 3 i changed the type to string