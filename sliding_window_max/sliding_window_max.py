'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# def sliding_window_max(nums, k):
#     # array for maximum numbers
#     maximums = []
#     for i in range(len(nums) - k + 1):
#         # loop thru the nums array and each time, update the array of the elements in the window
#         window = []
#         for num in range(k):
#             window.append(nums[i + num])
#         # set maximum for each element in window array
#         maximum = max(window)
#         # append it to maximums array and return it
#         maximums.append(maximum)
#     return maximums


def sliding_window_max(nums, k):
    current = 0
    maximums = []

    while k + current <= (len(nums)):
        maximums.append(max(nums[current:k+current]))
        current += 1
    return maximums


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

# UNDERSTAND
# there is a sliding window of a size which is represented by k
# its going to move from the beginning of the array, to the right,
# one element at a time.
# we need to return an array that has the largest value from each window.

# PLAN
# we are given 'k' (size), and the (initial) array.
# we will need an array for the max in each window
# also we will need an array for the window its self
# loop thru the nums array and each time, update the array of the elements in the window

# EXECUTE
# see above

# REFLECT
# this is ineffecient. O(n^2). it does not pass the large input test, only the initial test
