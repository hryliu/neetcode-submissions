class Solution {
public:
    int maxArea(vector<int>& heights) {
        // Time:  O(n)
        // Space: O(1)

        int area = 0;

        int left = 0;
        int right = heights.size() - 1;

        while (left < right){
            int new_area = (right - left) * min(heights[left], heights[right]);

            if (new_area > area){
                area = new_area;
            }

            if (heights[left] <= heights[right]) left++;
            else right--;
        }
        return area;
    }
};
