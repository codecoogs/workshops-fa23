class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int start = 0;

        int max_len = 0;

        unordered_map<char, int> freq;

        for (int end = 0; end < s.length(); end++){

            freq[s[end]]++;

            while (freq[s[end]] > 1){
                freq[s[start]]--;
                start++;
            }

            max_len = max(max_len, end-start+1);
        }

        return max_len;
        
    }
};