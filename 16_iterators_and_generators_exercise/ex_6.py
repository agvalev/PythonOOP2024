def fibonacci():
    curr_num, next_num = 0, 1
    while True:
        yield curr_num
        curr_num, next_num = next_num, curr_num + next_num

generator = fibonacci()

for i in range(10):

    print(next(generator))