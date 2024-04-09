class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        int index = 0;
        int size = nums.size();
        nums.push_back(INT_MIN);
        nums.push_back(INT_MIN);

        for(int i=0; i<size; i++){

            if(nums[i] == nums[i+1] && nums[i] == nums[i+2]){
                continue;
            }
            else{
                nums[index] = nums[i];
                index++;
            }
        }
 
        return index;
    }
};