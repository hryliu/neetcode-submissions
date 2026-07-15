class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // Time : O(n) - Each element is visited at most once by either pointer
        // Space: O(1) - Only two integer pointers are used
        int left = 0;
        int right = numbers.size() - 1;

        // Continue until the two pointers meet
        while (left < right) {
            // Calculate the sum of the two current numbers
            int sum = numbers[left] + numbers[right];

            // If the sum matches the target, return the pair
            // (depending on the problem, you might need indices instead)
            if (sum == target)
                return {left + 1, right + 1};

            // If sum is too large, move the right pointer leftward
            else if (sum > target)
                right--;

            // If sum is too small, move the left pointer rightward
            else
                left++;
        }

        // If no valid pair is found, return an empty vector
        return {};
    }
};
