# This file gets the current time in seconds, and then converts it to the 'Mour' time format.

import datetime
from fractions import Fraction

def get_mour_time(time = None):

    if time is None:
        time = datetime.datetime.now()
        
    MOUR_CONSTANT = Fraction(25, 21600) # 1 Mour = 25/21600 seconds, or 1 second = 86400/25 Mours from 100 Mours in a day

    midnight = datetime.datetime.combine(datetime.date.today(), datetime.time.min)

    elapsed_time_in_seconds = (time - midnight).total_seconds()

    elapsed_time_in_mour = elapsed_time_in_seconds * MOUR_CONSTANT

    return elapsed_time_in_mour



if __name__ == "__main__":
    # sample_time = datetime.datetime.combine(datetime.date.today(), datetime.time(4, 0, 0)) # sample time for testing at 4:00 AM
    sample_time = None
    mour_time = get_mour_time(sample_time)
    print( f"Mour time: {mour_time}" )
