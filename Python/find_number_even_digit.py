# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


def findNumbers(nums: list[int]) -> int:
    count = 0
    for i in range(len(nums)):
        if len(str(nums[i])) % 2 == 0:
            count += 1
    return count


def testes():
    print(findNumbers([555, 901, 482, 1771]))
    print(findNumbers([12, 345, 2, 6, 7896]))


if __name__ == "__main__":
    testes()
