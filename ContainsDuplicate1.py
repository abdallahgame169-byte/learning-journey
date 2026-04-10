class Solution(object):
    def containsDuplicate(self, nums):
        hasha = set()
        for n in nums:
            if n in hasha:
                return True
            hasha.add(n)
        return False