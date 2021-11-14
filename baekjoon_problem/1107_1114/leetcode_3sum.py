class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            answer = set()
            positive_nums = sorted([n for n in nums if n > 0])
            positive_nums_set = set(positive_nums)
            negative_nums = sorted([n for n in nums if n < 0])
            negative_nums_set = set(negative_nums)
            zero_nums = [n for n in nums if n == 0]

            # All zero
            if len(zero_nums) > 2:
                answer.add((0, 0, 0))

            # neg + zero + pos
            if len(zero_nums) > 0:
                for positive_num in positive_nums:
                    if -positive_num in negative_nums_set:
                        answer.add((-positive_num, 0, positive_num))

            # neg + neg + pos
            for i in range(len(negative_nums)):
                for j in range(i+1, len(negative_nums)):
                    add = -(negative_nums[i] + negative_nums[j])
                    if add in positive_nums_set:
                        answer.add((negative_nums[i], negative_nums[j], add))

            # neg + pos + pos
            for i in range(len(positive_nums)):
                for j in range(i+1, len(positive_nums)):
                    add = -(positive_nums[i] + positive_nums[j])
                    if add in negative_nums_set:
                        answer.add((positive_nums[i], positive_nums[j], add))

            return list(answer)