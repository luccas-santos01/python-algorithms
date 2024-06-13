def find_duplicate(nums):
    if not isinstance(nums, list):
        return False
    seen = set()
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if num in seen:
            return num
        seen.add(num)
    return False
