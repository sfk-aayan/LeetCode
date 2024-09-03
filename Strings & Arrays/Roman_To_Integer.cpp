class Solution {
public:
    int romanToInt(string s) {
        unordered_map <char, int> mp;

        mp['I'] = 1;
        mp['V'] = 5;
        mp['X'] = 10;
        mp['L'] = 50;
        mp['C'] = 100;
        mp['D'] = 500;
        mp['M'] = 1000;

        int sum = 0;
        int len = s.size();

        for(int i = 0; i<len-1; i++){
            if(mp[s[i]] < mp[s[i+1]]){
                sum -= mp[s[i]];
                continue;
            }
            sum += mp[s[i]];
        }
        sum += mp[s[len-1]];
        return sum;
    }
};