class Solution {
public:
    // Time: O(nlogm) - O(n) over piles, binary search ranges over speeds [1 … m] where m = max(piles)
    // Space: O(1)
    bool isPossible(vector<int>& piles, int h, int k){
        int hours = 0;
        
        for (int p : piles){
            hours += (p + k - 1) / k;
            if (hours > h) return false;
        }

        return hours <= h;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = *max_element(piles.begin(), piles.end());;

        while (low < high){
            int mid = (low + high) / 2;
            if (isPossible(piles, h, mid)) high = mid;
            else low = mid + 1;
        }
        return low;
    }
};
