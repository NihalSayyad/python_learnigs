
even_number = [i for i in range(11) if i%2 == 0]
print(even_number)

odd_number = [i for i in range(11) if i%2 != 0]
print(odd_number)

#flatening three dimentional list 

three_dimen_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in three_dimen_list for number in row]
print(flattened_list)