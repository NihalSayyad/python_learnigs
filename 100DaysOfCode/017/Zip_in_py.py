'''
Sometimes we would like to combine lists when looping through them
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})
    #Carrot will be skipped as it is beyond the index.

print(fruits_and_veges)