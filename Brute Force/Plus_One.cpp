class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry_flag = 0;
        
        for(int i = digits.size()-1; i>=0; i--){
            if(digits[i] == 9 && carry_flag != 1){
                digits[i] = 0;
                continue;
            }

            if(carry_flag == 0){
                digits[i]++;
                carry_flag = 1;
            }
        }
        if(!carry_flag){
            digits.insert(digits.begin(), 1);
        }

        return digits;
    }
};