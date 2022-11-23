import math
from decimal import Decimal

def output(theta0, iteration, choice):
    a,b = 2,5 # values for a and b are set to default for 2 division if choice was for 5 division we cange the values

    if choice==5:  
        a,b = b,a  # a,b = 5,2  / exchanging the values of a and b together if the choice was 5

    theta1 = theta0
    output = delta = beta = 0

    # finding how many dividable by a it has
    for m in range (0, math.floor(math.log(theta0,a))):
        if (theta0/(pow(a,m)))%a == 0:
            delta += 1

    # finding sum of the digits
    for j in range (1, iteration+1):
        beta += math.floor(math.log10( (theta0*pow(b,j)/pow(10,delta)) if theta0%pow(a,j) !=0 else (theta0*pow(b,j)/pow(10,j)) )+1)
    
    # calculating the output
    for i in range (0 , iteration+1):
        
        if theta0/pow(a,i) < 1:                                               # adding the zeroes 0.007b adding 3 zeroes
            output = output*pow(10,int(-math.log10(theta0/pow(a,i))+1))

        output += int(theta1*pow(10,beta))                                    # adding the values to output    * pow(10,(int(-math.log10(theta0/pow(a,i))+1) if theta0/pow(a,i) < 1 else 0))
        theta1 = int(theta1/a if theta1%a == 0 else  theta1*b )               # updating the theta1 to the next number
        
        beta -= math.floor((math.log10(theta1)+1))                            # updating alpha with removing digit counts of current number

    return output



"""RUN SEction"""

theta0 = int(input("Number: "))

choice = int(input("5 or 2 ? "))
while choice != 5 and choice != 2:                                                                     # Choice value should be either 2 or 5
    choice = int(input("5 or 2 ?  (please enter either 2 or 5): "))

iteration = int(input("Iterations: "))
while iteration%2 == 0:                                                                                # number of iterations ahould be an odd number, you can make this if rule as a comment if you want to test with even numbers
    iteration = int(input("Iterations (please enter an odd number): ")) 

output = int( output(theta0, iteration, choice) )                                                      # giving the whole number with respect to odd or even function

print("Result:", output, '\n', "= 3 * %s and division remainder = %f" %(Decimal(output)/3,output%3))    # for having the exact deciaml values after decimal point i changed the output type to Decimal, and because it was big to be a float type when deviding by 3 i changed the type to string