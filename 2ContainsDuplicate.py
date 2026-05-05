nums = [2, 6, 4, 8, 3, 7, 2, 9]


def ContainsDuplicate(paramList):
    """
    Returns true if the list contains duplicate, else false.

    :param paramList: list of integers
    """
    myDictionary = {}
    for num in paramList:
        if num in myDictionary:
            return True
        myDictionary[num] = True

    return False


if __name__ == "__main__":
    result = ContainsDuplicate(nums)
    print(result)
