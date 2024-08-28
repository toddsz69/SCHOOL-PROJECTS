def sort_characters(s):
    char_list = list(s)
    char_list.sort()
    sorted_string = ''.join(char_list) 
    return sorted_string

input_string = "CANICOMP"
sorted_string = sort_characters(input_string)
print(f"String sebelum diurutkan: {input_string}")
print(f"String setelah diurutkan: {sorted_string}")