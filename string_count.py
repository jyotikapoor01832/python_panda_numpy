def compute(str1):
    char_count=0
    digit_count=0
    symbol_count=0
    for char in str1:
        if char.isalpha():
            char_count+=1
        elif char.isdigit():
            digit_count+=1
        else:
            symbol_count+=1
    print("Count of letter is : ",char_count)
    print("Count of digit is : ", digit_count)
    print("Count of symbol is : ",symbol_count)

str1= "gitversion 2.43.0.windows.1"
compute(str1)