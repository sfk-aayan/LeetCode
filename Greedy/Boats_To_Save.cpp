class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int left = 0, result = 0;
        int right = people.size()-1;
        int remaining;

        while(left <= right){
            remaining = limit - people[right];
            right--;
            result++;

            if(left <= right && remaining >= people[left]){
                left++;
            }
        }
        return result;
    }

};