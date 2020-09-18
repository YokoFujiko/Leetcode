'''给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]'''



def twoSum(nums,target):
    lens=len(nums)
    j=-1
    for i in range(lens):
        if(target-nums[i]) in nums:
            if (nums.count(target-nums[i])==1)&(target-nums[i]==nums[i]):
                #如果等于（target-num【i】的数字只有一个，并且和num【i】是同一个东西就不要）
                continue
            else:
                j=nums.index(target-nums[i],i+1)#index从i+1找起
                break
    if j>0:
        return [i,j]
    else:
        return []