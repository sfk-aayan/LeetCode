class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int new_pos, temp;
        int size = nums.size();
        int arr[size + 1];

        for(int i=0; i<size; i++){
            new_pos = (i + k + 1) % size;
            if(new_pos == 0){
                arr[size - 1] = nums[i]; 
            }
            else{
                arr[new_pos - 1] = nums[i];
            } 
        }

        for(int i =0; i<size; i++){
            nums[i] = arr[i];
        }
    }
};