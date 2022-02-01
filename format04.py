#조합하기 1

output_h = "{:+5d}".format(52) #기호를 뒤로 밀기: 양수 
output_i = "{:+5d}".format(-52) #기호를 뒤로 밀기: 음수 
output_j = "{:=+5d}".format(52) #기호를 앞으로 밀기: 양수 
output_k = "{:=+5d}".format(-52) #기호를 앞으로 밀기: 음수 
output_l = "{:+05d}".format(52) #0으로 채우기:양수 
output_m = "{:+05d}".format(-52) #0으로 채우기: 음수 

print("#조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

#숫자 앞에 0 넣으면 0으로 채우기 가능 
#기호 앞으로 밀 땐 =부터 =+