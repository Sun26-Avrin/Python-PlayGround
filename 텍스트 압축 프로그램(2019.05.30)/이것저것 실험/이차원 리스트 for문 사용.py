#이차원 리스트 for문 사용

code = []
cnt = 0
for i in range(4) :
    code.append([])
    code[i].append(cnt)
    cnt += 1
    code[i].append(cnt)
    cnt += 1


for letter in code :
    print(letter)
#letter 은 일차원 배열을 반환 

#이차원리스트 len 반환값

print(len(code))
