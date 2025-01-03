class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector <int> ans(len);
        ans[0] = 1;
        for(int i = 1; i < len; i++){
            ans[i] = ans[i-1] * nums[i-1];
        }

        int postfix = 1;
        for(int i = len-1; i>=0; i--){
            ans[i] *= postfix;
            postfix *= nums[i]; 
        }

        return ans;
    }
};