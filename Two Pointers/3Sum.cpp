class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
           sort(nums.begin(), nums.end());
           set <vector<int>> temp;
           vector <vector<int>> ans;
           int len = nums.size();

           for(int i = 0; i < len; i++){
            int left = i + 1;
            int right = len - 1;

            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];

                if(sum == 0){
                    temp.insert({nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                }
                else if(sum > 0){
                    right--;
                }
                else{
                    left++;
                }
            }

           }

           for(auto x : temp){
            ans.push_back(x);
           }
           return ans;
    }
};