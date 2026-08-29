def get_squared_evens(nums):
    return[n*n for n in nums if n%2==0]
nums=[1,2,3,4,5,6,7,8]
print(get_squared_evens(nums))