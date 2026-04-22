
#To avoid brute force solution we use a dict to avoid a loop inside another loop
#This is a O(n) where the efficient depends of the number of dataset that we have .
def twoSum(nums, target):

    n = len(nums)
    result = []
    oldNumber = {}

    for i in range(0,n):
        the_value = target - nums[i]

        if the_value in oldNumber:
            result.append(i)
            result.append(oldNumber[the_value])
        else:
            oldNumber[nums[i]] = i

    return result

print(twoSum([2,7,11,15],9))