# 리스트 안 리스트 \n 제거 

for i in range(0, len(main_txt)):
  for j in range(0, len(main_txt[i])):
   change_sentence = (str(main_txt[i][j]).replace('\n', ' '))
   change_list.append(change_sentence)
  
  newmain_txt.insert(i, change_list)

print(newmain_txt[1])
len(newmain_txt)