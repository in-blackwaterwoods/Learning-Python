#문제 4

str_input = input("숫자 입력> ")
num_input = float(str_input)

print()
print(num_input, "inch")
print((num_input * 2.54), "cm")

#문제 5
str_input = input("원의 반지름 입력> ")
num_input = float(str_input)
print()
print("반지름: ", num_input)
print("둘레: ", 2 * 3.14 * num_input)
print("넓이: ", 3.14 * num_input ** 2)

#문제 6
a = input("문자열 입력> ")
b = input("문자열 입력> ")

print(a, b)

c = [a, b]
a = c[1]
b = c[0]

print(a, b)



