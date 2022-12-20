"""

Author: Kapish Patel
Aim:
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
NOTE:
    Used set data structure to compare length of set and list
    because set do not allow duplicates values so, using that property we can eliminate for loops to decrease complexity

"""


class Solution(object):
    @staticmethod
    def contains_duplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = set(nums)    # created a new set from old list
        if len(temp) == len(nums):  # check the length of set and list and return value as per required
            return False
        return True


def main():
    print('217: Contains Duplicate - EASY')
    lst = [1, 5, 3, 7, 3, 8, 6, 4, 6, 2, 7, 9, 4, 5, 2, 5, 0]
    sol = Solution()
    answer = sol.contains_duplicate(lst)
    print(answer)


if __name__ == "__main__":
    main()
