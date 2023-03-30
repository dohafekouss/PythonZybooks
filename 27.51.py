def digit_to_char(single_digit):
    digit_as_char = chr(ord('0') + single_digit)
    return digit_as_char


def num_to_string_with_commas(user_num):
    curr_num = user_num
    num_as_string = ""
    pos_count = 0

    while curr_num > 0:
        if pos_count == 3:
            num_as_string = ',' + num_as_string
            pos_count = 1
        else:
            pos_count += 1
        curr_digit = curr_num % 10
        curr_digit_as_char = digit_to_char(curr_digit)
        num_as_string = curr_digit_as_char + num_as_string
        curr_num //= 10

    if user_num == 0:
        num_as_string = '0'

    return num_as_string
user_num = int(input())
result_string = num_to_string_with_commas(user_num)
print(result_string)