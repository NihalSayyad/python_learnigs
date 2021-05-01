def sum_numbers(nums):
    print(type(nums))
    return sum(nums)

def high_order_function(f, *args):
    summation = f(*args)
    return summation

result = high_order_function(sum_numbers, [1,2,3,4,5])
print(result)