import random

class primeNumber(object):
    def __init__(self, n):
        self.n = n
    def isPrime(self):
        for k in range(2, self.n+1):
            if self.n % k == 0:
                break
        if self.n == k:
            return True
        else:
            return False


a = random.randint(1, 20 + 1)
print(a)
prime=primeNumber(a)
print(f'{prime.n} is Prime numbers') if prime.isPrime() else print(f'{prime.n} is not Prime numbers')