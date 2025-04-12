class Solution {
public:
    bool possible(int speed, const vector<int>& piles, int h) {
        int hour = 0;
        for (int pile : piles) {
            hour += ceil(pile / (double)speed);
        }
        return hour <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());

        while (l < r) {
            int mid = (l + r) / 2;
            if (possible(mid, piles, h)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }
};