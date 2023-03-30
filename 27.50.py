def digits_to_num(digits_list):
    curr_weight = 1
    total_num = 0

    for digit in reversed(digits_list):
        total_num += digit * curr_weight
        curr_weight *= 10

    return total_num
digits_list = list(map(int, input().split()))
result_num = digits_to_num(digits_list)
print(result_num)