class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len = nums.size();
        int goal = nums[len - 1];

        for(int i = len-1; i>=0; --i){
            if(i + nums[i] >= goal){
                goal = i;
            }
        }
        return (goal > 0) ? false: true;
    }
};