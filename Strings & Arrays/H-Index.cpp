class Solution {
public:
    int hIndex(vector<int>& citations) {
        int max_len = citations.size();
        sort(citations.begin(), citations.end(), greater<int>());

        int max = 0;
        for(int i = 0; i < max_len; i++){
            if(i + 1 <= citations[i] && i + 1 > max){
                max = i + 1;
            }
        }

        return max;

    }
};