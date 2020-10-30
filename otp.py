import random
import time

def otp():
    s="0123456789"
    passlen=6
    otp="".join(random.sample(s,passlen))
    time.sleep(1)
    return(otp)
