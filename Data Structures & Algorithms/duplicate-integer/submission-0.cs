public class Solution {
    public bool hasDuplicate(int[] nums) {
        var duplicateDict = new Dictionary<int, int>();

        foreach(var num in nums) {
            if(duplicateDict.ContainsKey(num)) {
                return true;
            }

            duplicateDict[num] = num;
        }

        return false;
    }
}