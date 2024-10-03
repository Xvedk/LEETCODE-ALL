vector<int> findMajority(vector<int>& nums) {
    unordered_map<int, int> freq;
    vector<int> result;
    int threshold = nums.size() / 3;
    
    // Count the frequency of each number
    for (int num : nums) {
        freq[num]++;
    }

    // Add numbers to result if their count exceeds the threshold
    for (const auto& entry : freq) {
        if (entry.second > threshold) {
            result.push_back(entry.first);
        }
    }

    // Sort the result and return, or return {-1} if no majority elements
    if (!result.empty()) {
        sort(result.begin(), result.end());
        return result;
    }
    
    return {-1};
}
