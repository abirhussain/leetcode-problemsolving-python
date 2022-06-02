    def buildArray(self, nums: List[int]) -> List[int]:
        length_of_nums = len(nums)
        ans = [None]*length_of_nums
        for i in range(0, length_of_nums):
            ans[i] = nums[nums[i]]
        return ans
