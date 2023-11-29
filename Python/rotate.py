#Reprovado por timeout

# def cycle(nums):
#     temp = nums[:]
#     nums[0] = temp[-1]
#     for i in range(1, len(nums)):
#         nums[i] = temp[i-1]
#     print(nums)


# nums = [1,2,3,4,5,6,7]
# cycle(nums)
# cycle(nums)
# cycle(nums)

# k = k % len(nums)
# nums[:] = nums[-k:] + nums[:-k]


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


# x = Solution()

# ls = [1,2,3,4,5,6,7]

# x.rotate(ls, 1)
# print(ls)