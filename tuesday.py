# Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target.

# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.

# EXAMPLE
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # instantiate an empty dictionary
        required = {}
        # loop through the indices of the nums
        for i in range(len(nums)):
            # if the target minus the num at the specified index is in required
            if target - nums[i] in required:
                # return the difference at the specified index
                return [required[target - nums[i]], i]
            # else
            else:
                # set the value in required, at the specified index, equal to
                # i 
                required[nums[i]] = i


nums = [2, 7, 11, 15]
solution = Solution()

print(solution.twoSum(nums, 9))