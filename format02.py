#정수 

output_a = "{:d}".format(52)

#특정 칸에 출력하기 
output_b = "{:5d}".format(52)  #5칸
output_C = "{:10d}".format(52)  #10칸

#빈 칸을 0으로 채우기 
output_d = "{:05d}".format(52) #양수
output_e = "{:05d}".format(-52) #음수 

print("# 기본")
print(output_a)
print("\n#특정 칸에 출력하기")
print(output_b)
print(output_C)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

#:d로 적을 땐 매개변수로 정수만 올 수 있음 
#특정 칸 원할 때는 숫자 적기 
