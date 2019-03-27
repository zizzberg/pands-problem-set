
#import datetime #import datetime 

#print("%A, %B, %d, %Y, %H, %I, %p")) 
# datetime.now().strftime
# Converts timestamp to required format but throwing a weird mismatch with minutes. 

#alt 
import datetime
#now = datetime.datetime.today() # current date and time - incorrect time
x = datetime.datetime.now()


print(x.strftime("%A %B %d %Y at %H %I %p")) 