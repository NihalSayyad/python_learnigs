import multiprocessing

result = []

def calc_square(numbers, result, v):
    v.value = 9.99
    for idx, n in enumerate(numbers):
        result[idx] = n*n


if __name__ == '__main__':
    numbers = [2,3,4,5]
    result = multiprocessing.Array('i', 4)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers,result,v))

    p.start()
    p.join()

    print(result[:])
    print(v)
    print(v.value)