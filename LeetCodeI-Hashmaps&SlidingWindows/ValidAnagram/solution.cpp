class Solution {
public:
    bool isAnagram(string s, string t) {
         
         unordered_map <char, int> mp_s;

         for (auto c: s){
             mp_s[c]++;
         }

         unordered_map <char, int> mp_t;

         for (auto c: t){
            mp_t[c]++;
         }
         
         return mp_t == mp_s;
    }
};