#inter a positive integer and tell user whether prime is not 
unum = int(input("Enter a positive integer to see whether it is prime: "))

if unum > 1:
    for i in range(2, unum): 
        if (inum % i) == 0: # modulo = 0 = no prime
        print (inum, "not a prime")
        break # exit loop - next statement 

    else: 
        print(inum, "is a prime")

else: 
    print(inum, "not a prime")
       