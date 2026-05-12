class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] result = new int[2];
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i = 0; i < nums.length; i++) {
            int mapTarget = target - nums[i];
            if (map.containsKey(mapTarget)){
                result[0] = map.get(mapTarget);
                result[1] = i;
            }
            map.put(nums[i], i);
        }
        return result;
    }
}
