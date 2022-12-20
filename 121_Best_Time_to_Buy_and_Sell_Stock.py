from typing import List
print('121: Best time to buy and sell stocks - EASY')

a = [1, 3, 6, 3, 7, 2]


class Solution:
    def maxprofit(self, prices: List[int]) -> int:


    @staticmethod
    def getindex(price, target):
        index = price.index(target)
        return index


def main():
    calc = Solution()
    calc.maxprofit(a)


if __name__ == "__main__":
    main()
