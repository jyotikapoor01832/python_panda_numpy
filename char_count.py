str="Hello"
char_dict=dict()
for char in str:
    count=str.count(char)
    char_dict[char]=count
print("Result is :", char_dict);