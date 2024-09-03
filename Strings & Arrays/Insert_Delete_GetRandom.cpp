class RandomizedSet {
    unordered_map <int, int> mp;
    vector <int> arr;
   
public:
    RandomizedSet() {

    }
    
    bool insert(int val) {
        if(mp.find(val) != mp.end()){
            return false;
        }
        mp[val] = arr.size();
        arr.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if(mp.find(val) != mp.end()){
            auto it = mp.find(val);
            int pos = it->second;

            if(pos != arr.size()-1){
                int lastElement = arr[arr.size()-1];
                swap(arr[arr.size()-1], arr[pos]);
                arr.pop_back();
                mp[lastElement] = pos;
                mp.erase(val);
                return true;
            }
            else{
                arr.pop_back();
                mp.erase(val);
                return true;
            }
        }
        return false;
    }
    
    int getRandom() {
        int randomPos = rand() % arr.size();
        return arr[randomPos];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */