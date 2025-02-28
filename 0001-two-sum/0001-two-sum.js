/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var remainder = {}

    for (let idx = 0; idx < nums.length; idx++) {
        var num = nums[idx];
        var other = target - num;
        if (other in remainder) {
            return [remainder[other], idx];
        } 
        remainder[num] = idx;
    }
};

