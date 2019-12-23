class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        two_sum = []
        out = set()
        dct = {}
        del_list = []
        #checked = set()
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = [i]
            elif len(dct[nums[i]]) < 3:
                dct[nums[i]].append(i)
            elif len(dct[nums[i]]) >= 3:
                del_list.append(nums[i])
        for i in del_list:
            nums.remove(i)
        dct = {}
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = [i]
            elif len(dct[nums[i]]) < 3:
                dct[nums[i]].append(i)
            elif len(dct[nums[i]]) >= 3:
                del_list.append(nums[i])
        
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                #if (nums[i], nums[j]) not in checked:
                two_sum.append((j, nums[i]+nums[j]))
                    #checked.add((nums[i], nums[j]))
                
        for i in range(len(two_sum)):
            if -two_sum[i][-1] in dct:
                if dct[-two_sum[i][-1]][-1] > two_sum[i][0]:
                    a = sorted((-nums[two_sum[i][0]]+two_sum[i][-1], nums[two_sum[i][0]], -two_sum[i][-1]))
                    out.add((a[0],a[1],a[2]))
        return out