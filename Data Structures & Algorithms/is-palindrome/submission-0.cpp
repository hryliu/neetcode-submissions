class Solution {
public:
    bool isPalindrome(string s) {
        // Time: O(n)
        // Space: O(1) - using two pointer technique directly on string
        int left = 0;
        int right = s.size() - 1;

        while (left < right) {
            // Move left pointer forward until we find an alphanumeric character
            while (left < right && !isalnum(s[left])) left++;
            // Move right pointer backward until we find an alphanumeric character
            while (left < right && !isalnum(s[right])) right--;

            // Compare lowercase versions
            if (tolower(s[left]) != tolower(s[right]))
                return false;  // mismatch → not a palindrome

            left++;
            right--;
        }

        return true; // all matched → palindrome
    }
};
