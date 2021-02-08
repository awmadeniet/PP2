class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum = 0
        sum = 0
        for i in range(len(gain)):
            sum = sum + gain[i]
            if maximum < sum:
                maximum = sum
        return maximum