# -*- coding: utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        result = sorted(nums1)
        number = len(result)
        if number / 2 == number / 2.0:
            return (result[number / 2 - 1] + result[number / 2]) / 2.0
        else:
            return result[number / 2]
