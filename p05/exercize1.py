import random
# range()
#
# for i in range(5):
#     print(i, end=' ')
#
# print()
# for i in range(2, 5):
#     print(i, end=' ')
#
# print()
# for i in range(4, 11, 2):
#     print(i, end=' ')

# start_range = int(input('Start :'))
# end_range = int(input('End :'))
# step_range = int(input('Step :'))
#
# for k in range(start_range, end_range, step_range):
#     print(k, end=',')


# for i in range(101):
#     x = random.randint(0, 100)
#     print(x, end='')


# for j in range(1, 10):
#     print()
#     for i in range(1, 10):
#         print(f'{j}*{i}={j*i}', end=' ')

start_range = int(input('Start:'))
end_range = int(input('End: '))
for n in range(start_range, end_range + 1):
    is_prime = True

    # n = 7
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print('%d, ' % n, end='')
