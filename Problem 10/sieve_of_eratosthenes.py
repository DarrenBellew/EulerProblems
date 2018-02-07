from datetime import datetime
from math import sqrt, floor

starttime=datetime.now()

val = 2000000
stop = int(floor(sqrt(val)))
print("stop: " + str(stop))
sieve = [x for x in range(2,val)]

def remove_nonprimes(sieve, p):
    markset = set(sieve[p-2::p][1::])
    sieve = list(filter(lambda x: x not in markset, sieve))
    return sieve

for p in range(2, stop):
    if(p in sieve):
        sieve=remove_nonprimes(sieve, p)

print(str(sum(sieve)))

timeelapsed=datetime.now()-starttime
print("time elapsed (hh:mm:ss.ms) {}:".format(timeelapsed))
