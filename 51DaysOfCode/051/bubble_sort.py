
def bubble_sort(element):

    size = len(element)

    for i in range(size-1):
        if element[i] > element[i+1]:
            temp = element[i]
            element[i] = element[i+1]
            element[i+1] = temp

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]

    bubble_sort(elements)
    print(elements)