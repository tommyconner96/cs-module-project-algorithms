'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


# UNDERSTAND
# we are given a number of cookies, n
# how many ways can the cookies be eaten?
# ex: n = 3
#  1. He can eat 1 cookie at a time 3 times
#  2. He can eat 1 cookie, then 2 cookies 
#  3. He can eat 2 cookies, then 1 cookie
#  4. He can eat 3 cookies all at once. 
# so eating_cookes(3) should return 4
# there is a large input test and a small input test. the large one may require more
# optimization

# PLAN


