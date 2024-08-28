class Solution {
public:
    int jump(vector<int>& nums) {
        int min = 0;
        int len = nums.size();

        int l = 0;
        int r = 0;

        if(len == 1){
            return 0;
        }

        for(int i = 0; i<len; i++){
            l = max(l, i + nums[i]);

            if(r == i){
                r = l;
                min++;

            if (l >= len-1){
                break;
            }
            }
        }
        return min; 
    }
};