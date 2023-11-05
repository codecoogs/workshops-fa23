class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = strs[0];

        for (int i = 1; i < strs.size(); i++){
            string str = strs[i];
            string temp = "";

            int j = 0;

            while (j < min(str.length(), prefix.length()) && str[j] == prefix[j]){
                temp+=str[j];
                j++;
            }
            prefix = temp;
        }

        return prefix;
    }
};