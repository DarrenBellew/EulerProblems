#intro
print("The sieve of Eratothenes - by Darren Bellew")

#sievenum = input("Number to sive primes for: ")
sievenum = 23

sieve = [x for x in range(2,sievenum)]
p=2

sieve_notprime = sieve[p-2::p]

print(str(sieve_notprime))

p=5
sieve_notprime.extend(sieve[p-2::p])

print(str(sieve_notprime))
