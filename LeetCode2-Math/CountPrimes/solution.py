class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n is 0:  
            return 0

        isPrime = [True]*n

        for i in range(2,n):
            if isPrime[i]:
                for j in range(i*2, n, i):
                    isPrime[j] = False
                

        count = 0

        for i in range(2,n):
            if isPrime[i]:
                count+=1

        return count
        