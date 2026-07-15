class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Time:  O(n^2)
        // Space: O(1)

        vector<vector<int>> triplets;

        // Time: O(nlogn)
        sort(nums.begin(), nums.end());

        // Time: O(n^2)
        // Iterate through list
        for (int i = 0; i < nums.size(); i++){
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int j = i + 1;              // left
            int k = nums.size() - 1;    // right

            while (j < k){
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0){
                    triplets.push_back({nums[i], nums[j], nums[k]});

                    // Skip duplicates for j and k
                    while (j < k && nums[j] == nums[j + 1]) j++;
                    while (j < k && nums[k] == nums[k - 1]) k--;

                    j++;
                    k--;
                }
                else if (sum > 0) k--;
                else j++;
            }
        }
        return triplets;
    }
};
