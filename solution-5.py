#inter a positive integer and tell user whether prime is not 
unum = int(input("Enter a positive integer to see whether it is prime: "))

if unum > 1:
    for i in range(2, unum): 
        if (unum % i) == 0: # modulo = 0 = no prime
            print (unum, "not a prime")
            break # exit loop - next statement 

    else: 
        print(unum, "is a prime")

else: 
    print(unum, "not a prime")
       