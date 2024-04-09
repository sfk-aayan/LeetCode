class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> s;
        vector<int> remaining;

        for(auto i: nums){
            if(s.find(i) != s.end()){
                remaining.push_back(i);
                continue;
            }
            s.insert(i);
        }

        nums.clear();

        for(auto i: s){
            nums.push_back(i);
        }

        for(auto i : remaining){
            nums.push_back(i);
        }

        return s.size();

    }
};