class Solution {
public:
    bool isPowerOfThree(int n) {
        
    if (n <= 0) {
        return false;
    }
    
    double result = log(n) / log(3);
    
    // Check if the result is very close to an integer (within a small epsilon)
    return std::abs(result - round(result)) == 0;
    }
};