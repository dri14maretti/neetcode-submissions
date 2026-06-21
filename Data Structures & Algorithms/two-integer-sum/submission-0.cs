public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var ComplementDict = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++)
        {
            if(ComplementDict.ContainsKey(nums[i])) {
                return new int[2] {ComplementDict[nums[i]], i};
            }

            ComplementDict[target - nums[i]] = i;
        }

        return null;
    }
}
