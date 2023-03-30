def find_next_substr(s, start_index, substr):
    found_at_index = -1
    for i in range(start_index, len(s) - len(substr) + 1):
        substr_same = True

        for j in range(len(substr)):
            if s[i + j] != substr[j]:
                substr_same = False
                break

        if substr_same:
            found_at_index = i
            break

    return found_at_index
input_string = input()
start_index = int(input())
search_string = input()
print(find_next_substr(input_string, start_index, search_string))