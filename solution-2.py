# begins with a t - 0 mon, 1 tue, 3 thursday

import datetime

dayis = datetime.datetime.today().weekday()

if dayis == 1, 3: 
    print "Today begins with a T, Taco Tuesday or Terrific Thursday"

else: 

    print "Today doesn't being with a T"
