class solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        ans = []
        if len(nums1) == 0:
            ans = nums2
        elif len(nums2) == 0:
            ans = nums1

        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i = i + 1
            else:
                ans.append(nums2[j])
                j = j + 1
            if i == len(nums1):
                ans.extend(nums2[j:])
            elif j == len(nums2):
                ans.extend(nums1[i:])
        temp = (len(nums1) + len(nums2))
        if temp%2 == 1:
            return ans[int(temp/2)]
        else:
            return (ans[int(temp/2)]+ ans[int(temp/2) - 1]) / 2
def main():
    nums1 = []
    nums2 = [3]
    print(solution().findMedianSortedArrays(nums1, nums2))

if __name__ == "__main__":
    main()
