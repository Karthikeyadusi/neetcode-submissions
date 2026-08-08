class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        index = []
        lists = []
        lenght = []
        unique = sorted(list(set(nums)))
        for i in range(0,len(unique)):
            if i == 0:
                index.append(i)
            elif unique[i-1] + 1 == unique[i]:
                continue
            else:
                index.append(i)
            # if next == sort[i+1]:
            #     count+=1
        for x in range(len(index)):
            if x+1 == len(index):
                lists.append(unique[index[x]:])
            else:
                lists.append(unique[index[x]:index[x+1]])
        for item in lists:
            lenght.append(len(item))
        return max(lenght)

        