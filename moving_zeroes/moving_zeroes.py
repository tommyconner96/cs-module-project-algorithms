'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    for _ in range(len(arr)):
        # Boolean for swapped status
        swapped = False
        # define i, current position in the array
        i = 0
        while i < (len(arr) - 1):
            # if elemt is a 0
            if arr[i] == 0:
                # move it up
                arr[i+1],arr[i] = arr[i],arr[i+1]
                # set swapped true to indicate it's been addressed
                swapped = True
            # increment
            i = i+1

        # IF swapped = false: stop
        if swapped == False:
            break

    return arr

# def bubble_sort(arr):
#     for _ in range(len(arr)):
#         # Boolean for swapped status
#         swapped = False
#         # define i, current position in the array
#         i = 0
#         # while i < length of array
#         # (logic from for loop below)
#         #         if arr[j] > arr[j+1]:
#         #           swap
#         #           set swapped to True
#         while i < (len(arr) - 1):
#             if arr[i] > arr[i+1]:
#                 arr[i],arr[i+1] = arr[i+1],arr[i]
#                 swapped = True
#             # increment
#             i = i+1

#         # IF swapped = false: stop
#         if swapped == False:
#             break

#     return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# UNDERSTAND
#  this function needs to move each non zero integer to the left side, leaving all The
#  zeros on the right side.
#  order of non-zeros does not matter

# PLAN
# we need to sort the array in a way that zeroes will be last.
# bubble sort can be used and modified slightly so that if arr[i] == 0
# it will be moved to the end

# EXECUTE
# see code above. Used a modified version of my iterative 
# bubble sort function from last week

# REFLECT
# there is likely a more effecient way to do this
