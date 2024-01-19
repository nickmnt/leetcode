class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(a, b):

            p = int(''.join([a,b]))
            q = int(''.join([b,a]))

            if p > q:
                return -1
            elif p < q:
                return 1
            else:
                return 0

        l = [str(x) for x in nums]
        return str(int(''.join(sorted(l, key=functools.cmp_to_key(compare)))))