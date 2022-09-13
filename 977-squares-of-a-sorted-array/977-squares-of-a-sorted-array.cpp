class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        vector<int> result(right + 1, 0);
        int itr = right;
        while (left <= right) {
            int left_square = nums[left] * nums[left];
            int right_square = nums[right] * nums[right];
            if (left_square < right_square) {
                result[itr] = right_square;
                right--;
            } else {
                result[itr] = left_square;
                left++;
            }
            itr--;
        }
        return result;
    }
};