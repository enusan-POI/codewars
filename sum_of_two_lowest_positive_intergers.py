def q1(numbers):
    sorted_list = sorted(numbers)
    answer_sum = sorted_list[0] + sorted_list[1]

    print(answer_sum)
    return answer_sum

q1([5, 8, 12, 18, 22])