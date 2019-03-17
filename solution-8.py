import datetime #import datetime 

x = datetime.datetime.now()
print(x.strftime("%A, %B, %Y, %H, %I, %p")) 
# Converts timestamp to required format but throwing a weird mismatch with minutes. 
