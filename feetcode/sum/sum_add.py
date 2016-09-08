# -*- coding: utf-8 -*-


def get_sum(nums, target):
    result = []
    for i in range(len(nums)):
        if target - nums[i] in result:
            return [nums.index(target - nums[i]), i]
        result.append(nums[i])


if __name__ == '__main__':
    print get_sum([8, 5, 7, 2, 0, 4, 3, 2], 3)
