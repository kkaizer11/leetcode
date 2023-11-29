def rem_element(nums, val):
    dup = 0
    for i in range(len(nums)):
        if val == nums[i]:
            dup +=1
    for i in range(dup):
        nums.remove(val)

# x = [2, 3 ,3, 4 ,3]
# print(x)
# rem_element(x, 3)
# print(x)