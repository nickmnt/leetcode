class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # if nums[l] < nums[r]:
            #     if target < nums[mid]:
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            # else:
            if nums[mid] >= nums[l]:
                # left side
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # right side
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
