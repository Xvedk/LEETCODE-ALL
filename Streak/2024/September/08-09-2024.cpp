class Solution {
  public:
    int minJumps(vector<int>&a) {
        // Your code here
        int n = a.size();
        if(a[0] == 0)
            return -1;
            
        int jumps = 0, mxreachable = 0, limit = 0;
        for(int i = 0; i < n - 1; i++){
            mxreachable = max(mxreachable, i + a[i]);
            if(i == limit){
                limit = mxreachable;
                jumps++;
            }
        }
        if(limit < n - 1)
            return -1;
        return jumps;
    }
};
