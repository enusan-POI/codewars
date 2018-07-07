def iq_test(numbers):
    #your code here
    num_list = numbers.split()
    num_list = list(map(int, num_list))
    count = 1
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            continue
        else:
            count += i

    print(count)

iq_test('9 45 1 35 35 15 23 43 15 18 41 45 43 9 19 3 35 15 11 27 21 49 39 17 23 3 17 17 33 21 5 1 19 33')