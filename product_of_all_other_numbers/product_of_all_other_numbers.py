'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # this array will contain the results of the product of all other nums
    final_arr = []
    #loop over lenght of orig. array
    for i in range(len(arr)):
        # copy of array in loop
        # * operator is used here so that we make it iterable
        new_arr = [*arr]
        # exclude the current index
        new_arr.pop(i)
        # print(new_arr)

        product = 1
        for each in new_arr:
            product *= each

        final_arr.append(product)

    return final_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

# UNDERSTAND
# we need a function that recieves an array of ints and returns an array
# with the products of all numbers in the array except for the current number
# ideally we wanna do this in o(n) time without usibng division

# PLAN
# well need to loop over the arr
# create a copy of the array in the loop that excludes the current index
# multiply each value by all other values... another for loop?
