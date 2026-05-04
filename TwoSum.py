list_a = [8, 5, 4, 15, 12, 7, 2, 9, 11, 6]
target_a = 7


def two_sum(nums, target):
    """Return indices of the two numbers such that they add up to target.
    """
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return "Cannot find indices of the two numbers such that they add up to target."  


if __name__ == "__main__":
    result = two_sum(list_a, target_a)
    print(result)
