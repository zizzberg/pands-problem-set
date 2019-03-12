#step one if current value of n is positive divide it by 2 - if it is odd - 
#multiply by 3 and add 1 - if 1 end program 

n = int(input("Input a positive integer: "))
#while loops repeat code but don't run n time - only until a condition is met
while n != 1: 

    print(n)

    if n % 2 == 0:  #even
        n = n / 2 
    else:
        n = n * 3 
        n = n + 1

print("1") # prints 1 at the end outside of loop to end program. 
