def find_next_char_in_string(s, start_index, c):
    char_found = False
    for i in range(start_index, len(s)):
        if s[i] == c:
            char_found = True
            break
    if char_found:
        return i
    else:
        return -1
input_string = input()
start_index = int(input())
search_char = input()

print(find_next_char_in_string(input_string, start_index, search_char))