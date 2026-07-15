class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Time : O(n)
        // Space: O(1)

        // int left = 0;
        // int right = 1;

        // int maxP = 0;

        // while (right < prices.size()){
        //     int profit = prices[right] - prices[left];
        //     maxP = max(maxP, profit);

        //     if (prices[left] > prices[right]) left = right;
        //     right++;
        // }

        // return maxP;

        int maxP = 0;
        int buy = prices[0];

        for(int i = 1; i < prices.size(); i++){
            int profit = prices[i] - buy;

            maxP = max(maxP, profit);
            buy = min(buy, prices[i]);
        }
        return maxP;
    }
};
