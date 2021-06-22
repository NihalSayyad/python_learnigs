import multiprocessing

result = []

def calc_square(numbers):
    global result
    for n in numbers:
        result.append(n*n)
    print("Inside the process: result : ", str(result))

if __name__ == '__main__':
    numbers = [2,3,4,5]
    p = multiprocessing.Process(target=calc_square, args=(numbers,))

    p.start()
    p.join()

    print('Outside process: result : ', str(result))