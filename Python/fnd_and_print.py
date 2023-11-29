def fnd_prnt(nums, val):
    x = []
    for i in range(len(nums)):
        if val == nums[i]:
            x.append(nums[i])
    print(x)

# x = [1, 2 , 3, 3 ,6, 3]

# fnd_prnt(x, 3)
