def twoSUM(nums,target):
    hashmap = {}
    for key, value in enumerate(nums):
        diff = target - value
        if diff in hashmap:
            return [hashmap[value], key]
        hashmap[value] = key


# x = [2,7,11,15]

# twoSUM(x)
