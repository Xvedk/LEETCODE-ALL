class Solution {
  public:

    // Note that the size of the array is n-1
    int missingNumber(int n, vector<int>& arr) {

        // Your code goes here
        //sum of ap series till nth term-
        //(n/2)(2a+(n-1)d)
        //where a is the starting value, d is the interval or gap
        //or could be used (n*(n+1))/2 only for this case
        return ((double)n/2)*((2)+(n-1))-accumulate(arr.begin(),arr.end(),0);
    }
};
