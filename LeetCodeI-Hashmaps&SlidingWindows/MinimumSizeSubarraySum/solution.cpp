class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {

        int sum = 0;

        int min_len = nums.size()+1;

        int start = 0;

        for (int end = 0; end < nums.size(); end++){
            sum += nums[end];
            while (sum >= target){
                min_len = min(min_len, end-start+1);
                sum -= nums[start];
                start++;
            }
        }

        if (min_len > nums.size()) return 0;

        return min_len;
        
    }
};