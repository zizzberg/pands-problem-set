# begins with a t - 0 mon, 1 tue, 3 thursday

import datetime

dayis = datetime.datetime.today().weekday()

if dayis == 1 or 3: 
    print ("Yay! Today starts with a T")

else: 

    print ("Today doesn't being with a T")
