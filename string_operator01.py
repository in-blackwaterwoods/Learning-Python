print("문자 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

#거꾸로 뒤에서부터 선택하기
print()
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])

#문자열 범위 선택 연산자(슬라이싱)
print("안녕하세요"[0:3]) #마지막 숫자 포함되지 않음!
print("안녕하세요"[0:2])
print("감사합니다"[3:5])
print("뭐하세요?"[2:4])

#문자열 범위 선택 연산자(생략)
print("안녕하세요"[2:])
print("감사합니다"[:2])