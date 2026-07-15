class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Time: O(log(m) + log(n)) = O(log(m*n))
        // Space: O(1)

        int m = matrix.size();
        if (m == 0 || matrix[0].empty()) return false;
        int n = matrix[0].size();

        int lo = 0, hi = m*n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int r = mid / n, c = mid % n;
            if (matrix[r][c] == target) return true;
            if (matrix[r][c] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return false;
    }
};
