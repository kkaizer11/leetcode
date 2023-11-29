def rm_dup(nums):
    dup = []
    for i in range(len(nums) -1 ):
        if nums[i] == nums[i + 1]:
            dup.append(nums[i+1])
    for j in range(len(dup)):
        nums.remove(dup[j])
    print(nums)


# x = [0,0,1,1,1,2,2,3,3,4]
# rm_dup(x)