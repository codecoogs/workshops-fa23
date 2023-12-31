class Solution {
public:
    int countPrimes(int n) {

        if (n==0) return 0;

        vector<bool> isPrime(n, true);

        for (int i = 2; i*i < n; i++){

            if (isPrime[i]){
                for (int j = i*2; j < n; j+= i){
                    isPrime[j] = false;
                }
            }

        }

        int count = 0;

        for (int i = 2; i < n; i++){
            if (isPrime[i]) count++;
        }

        return count;
        
    }
};