"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2

    for x in range(number_of_primes):
        primeFound = False

        while primeFound == False:
            prime = True

            for i in range(2, num):
                if num % i == 0:
                    prime = False

            if prime:
                list.append(num)
                primeFound = True

            num += 1

    return list
