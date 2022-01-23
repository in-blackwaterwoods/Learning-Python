#입력을 받습니다 
string = input("입력> ")

#출력합니다 
print("자료:", string)
print("자료형:", type(string))

print()

# input_error 
#입력을 받습니다 
string = input("입력> ")

#출력합니다 
print("입력 + 100:", string + 100)

#int_convert 
string_a = input("입력A: ")
int_a = int(string_a)

string_b = input("입력B: ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a +int_b)