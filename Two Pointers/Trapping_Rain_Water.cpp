class Solution {
public:
    int trap(vector<int>& height) {
        int leftMax = height[0];
        int rightMax = height[height.size()-1];

        int leftP = 0;
        int rightP = height.size() - 1;
        int sum = 0;

        while(leftP < rightP){
            if(leftMax < rightMax){
                sum += leftMax - height[leftP];
                leftP++;
                leftMax = max(height[leftP], leftMax);
            }
            else{
                sum += rightMax - height[rightP];
                rightP--;
                rightMax = max(height[rightP], rightMax);
            }
        } 
        return sum;
    }
};