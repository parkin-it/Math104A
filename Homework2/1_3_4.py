#Solution to problem 1.3: 4

n = 0
error = 1

#Run until error is less than 10^-3
while error >= .001:
    n = n+1
    sum = 0
    
    #compute the summation for the series
    for i in range(1,n+1):
        sum_a = ((-1)**(i+1))*((1/2**(2*i-1))/(2*i-1))
        sum_b = ((-1)**(i+1))*((1/3**(2*i-1))/(2*i-1))
        sum = sum_a+sum_b+sum
    
    #Compute the value of pi
    pi_est = sum*4
    print(pi_est)
    
    #Find the error between the calculated and actual value of pi
    error = abs(math.pi - pi_est)
    
    print(error)
        

print(n)