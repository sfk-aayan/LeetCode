class Solution {
public:
    int climbStairs(int n) {
        int arr[n+1];
        arr[0] = 1;
        arr[1] = 2;

        for(int i = 1; i<n-1; i++){
            arr[i+1] = arr[i] + arr[i-1]; 
        }
        return arr[n-1];
    }
};