'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # array, for keeping track of dupes
    seen_values = []
    # for each in ORIGINAL arr
    for dupe in arr:
        # uncomment to see the action of elements being added and removed upon duplicate
        # print(seen_values)
        if dupe in seen_values:
            # this will be run every time a duplicate is found
            # eventually leaving us with only the single number
            seen_values.remove(dupe)
        else:
            # this will be executed the first time a number is added 
            # (and only once, for the one with no dupe)
            seen_values.append(dupe)
    # our final answer will be found in seen_values[0] after everything loops through
    return seen_values[0]



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


# UNDERSTAND
# We are given an array (non empty) where every element appears twice except for one.
# There will always be only one odd number out

# PLAN
# make an array for dublicates. 
# duplicates array will start out empty
# we will iterate thru the original array
# numbers are added to seen_values and then when they are seen again,
# they are deleted. in the end returning seen_values[0] will leave us with
# the remaining single number.

# EXECUTE
# see code above

# REFLECT
# this is O(n^2) time complexity, so it is defeinitely not the most efficient solution.
# more effecient version coming soon.