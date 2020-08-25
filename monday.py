# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the 
# array, and it should return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = [nums.count(i) for i in set(nums)]
        for i in count:
            if i > 1:
                return print("True")
                break
            else:
                continue
    
        return print("False")


v1 = [1,2,3,1] # True
v2 = [1,2,3,4] # False
v3 = [1,1,1,3,3,4,3,2,4,2] # True

solution = Solution()
solution.containsDuplicate(v1)
solution.containsDuplicate(v2)
solution.containsDuplicate(v3)