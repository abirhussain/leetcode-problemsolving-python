    def removeDuplicates(self, nums: List[int]) -> int:
        length_of_nums = len(nums)
        if length_of_nums == 1:
            return 1
        left_pointer = 0
        for right_pointer in range(1, length_of_nums):
            if nums[left_pointer] != nums[right_pointer]:
                left_pointer = left_pointer + 1
                nums[left_pointer] = nums[right_pointer]
        return left_pointer + 1
