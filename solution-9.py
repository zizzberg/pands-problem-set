#file = open ("sonnet.txt", 'r')
#for line in file: 
    #print(line)

with open("sonnet.txt", "r") as f: #declare poem as file
    index = 0 #start at beginning 
    for line in f:
        index += 1 #increment
        if index % 2 == 0:
            print(line) #if even line print 

