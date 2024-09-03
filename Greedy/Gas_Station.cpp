class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int len = gas.size();
        int totalGas = 0;
        int totalCost = 0;

        for(int i =0; i<len; i++){
            totalGas += gas[i];
            totalCost += cost[i];
        }

        if(totalCost > totalGas){
            return -1;
        }

        
        vector <int> greedy(len);
        int marker = 0;

        for(int i = 0; i<len; i++){
            greedy[i] = gas[i] - cost[i];
        }

        int total = 0;

        for(int i =0; i<len; i++){
            total += greedy[i];
            if(total < 0){
                total = 0;
                marker = i+1;
            }
        }
        return marker;
    }
};