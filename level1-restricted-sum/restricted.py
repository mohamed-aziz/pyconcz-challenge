def restricted(nums):
    # Add your solution here
    if nums == []:
        return 0
    return restricted(nums[1:])+nums[0]
