class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int length = s.size();

        if(length == 0){
            return 0;
        }

        unordered_map <char, int> mp;
        int maxLen = INT_MIN;
        int left = 0;
        int right = 0;

        while (right < length){

            mp[s[right]]++;

            while(mp[s[right]] > 1){
                mp[s[left]]--;
                left++;
            }

            maxLen = max(maxLen, right - left + 1);
            right++;
        }

        return (maxLen != INT_MIN) ? maxLen : 1;
    }
};