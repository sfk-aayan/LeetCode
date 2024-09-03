class Solution {
public:
    int candy(vector<int>& ratings) {
        int len = ratings.size();
        vector <int> candy(len, 1);

        for(int i=1; i<len; i++){
            if(ratings[i] > ratings[i-1]){
                candy[i] = candy[i-1] + 1;
            }
        }
        
        for(int i = len-2; i>=0; i--){
            if(ratings[i] > ratings[i+1]){
                candy[i] = max(candy[i+1] + 1, candy[i]);
            }
        }

        int sum = 0;
        for(auto x: candy){
            sum += x;
        }
        return sum;
    }
};