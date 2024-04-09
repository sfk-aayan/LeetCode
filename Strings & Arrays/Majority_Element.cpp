class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        int ans;

        map <int, int> mp;

        for(auto x: nums){
            mp[x]++;
        }

        auto pr = max_element(mp.begin(), mp.end(), [](const auto &x, const auto &y) {
                    return x.second < y.second;
                });

        return pr->first;
    }
};