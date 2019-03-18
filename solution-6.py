#string thing
#sentence.split ?

usent = input("Write a sentence: ")
words = usent.split(" ") #split string into words

for i in range(0, len(words)): #each word
    if i % 2 == 1: 
        print(words[i], end=" ") #print every 2nd.



