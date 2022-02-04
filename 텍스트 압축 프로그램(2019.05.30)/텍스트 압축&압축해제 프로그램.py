import copy
import struct
import os

###############main###################
print("이 프로그램은 확장자가 txt인 파일만 압축을 지원합니다.")
file_name = input("압축할 파일의 파일명을 확장자 없이 입력하세요 : ")
file_name += ".txt"
f = open(file_name,"rt")

text = f.read()
#text = text.lower() #소문자로만들기
#text = "Hello, Every body"
#소문자로 만들었음 , 압축풀때 대문자로바꾸셈
f.close()








#########


letters = []
only_letters = []
for ch in text :
    if ch not in letters :
        freq = text.count(ch)
        letters.append(freq) #빈도수가 먼저
        letters.append(ch)
        only_letters.append(ch)

##
nodes = [] #2차원 
while len(letters) > 0 :
    nodes.append(letters[0:2])
    letters = letters[2:]
nodes.sort() #빈도수로 정렬 
huffman_tree = []#3차원 
huffman_tree.append(nodes)

####

def combine(nodes) :
    pos = 0
    newnode = []
    ##2 lowest nodes.
    if len(nodes)>1 :
        nodes.sort() #인덱스 0기준, 인덱스0값이 같으면 1기준
        # 0,1 기입 
        nodes[pos].append("0")
        nodes[pos+1].append("1")
        combined_node1 = (nodes[pos][0]+nodes[pos+1][0])  #호프만 루트 가중치
        combined_node2 = (nodes[pos][1]+nodes[pos+1][1])   #식별자 
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes = []
        newnodes.append(newnode)
        newnodes += nodes[2:]
        nodes = newnodes #update 얕은복사
        huffman_tree.append(nodes)
        combine(nodes)
        #print("#########################")

    return huffman_tree

newnodes = combine(nodes)

huffman_tree.sort(reverse = True)  #newnodes 랑 주소값 공유 

#### 체크


checklist = []
cnt = 0
for level in huffman_tree :
    for node in level :
        if node not in checklist :
            checklist.append(node)
        else :
            level.remove(node)
            #c_huff[cnt].remove(node)
    #cnt += 1

'''
else : #삭제가 왜안되지....아! 중간에 삭제되면서 인덱스가 줄어들어서
    #반복문이 끝까지 안가는거였음
    level.remove(node)
'''
        
        


### make binary codes
letter_binary = []
if len(only_letters) == 1 :
    letter_code = [ only_letters[0],"0" ]
    letter_binary.append( letter_code*len(text) )
else :
    for letter in only_letters :
        lettercode = ""
        for node in checklist :
            if len(node)>2 and letter in node[1] :
                lettercode = lettercode + node[2] #문자열붙여!
        letter_code = [letter,lettercode]
        letter_binary.append(letter_code)


##
bitstring = ""
for character in text :
    for item in letter_binary :
        if character in item :
            bitstring += item[1]




#########파일만들기
make_file = file_name[0:-4]

#cmp
bit_len = len(bitstring)
bytes_int = 4*8
cnt = 0
check_when_unpack = (bit_len//bytes_int) +1

make_file += ".cmp"
f = open(make_file,"wb")
         
for i in range( (bit_len//bytes_int) ) : #마지막1번더해야됨
    new_binary = bitstring[cnt:cnt+32]
    a=int(new_binary, base=2)
    w_binary = struct.pack('I',a)
    f.write(w_binary)
    cnt += 32
                
last_binary = bitstring[cnt:-1] + bitstring[-1] #잔여 비트스트링
                                                #마지막비트는 뒤에 0 앞에 0 주의할것.
last_len = len(last_binary)######
last_front_zero = 0
for i in range(last_len) :
    if last_binary[i] == '0' :
        last_front_zero += 1
    else :
        break



last_b_int = int(last_binary, base=2)
w_binary = struct.pack('l',last_b_int)
f.write(w_binary)

f.close()
#dat (메타데이터)

make_file =file_name[0:-4]
make_file += ".dat"
f = open(make_file,"wt")
for digit in letter_binary :
    f.write(str(digit))
f.close()
print()
print(" 압축이 완료되었습니다.\n 같은 폴더내의 cmp파일과 dat파일을 확인하세요.")
print()

##기록확인

##

def decoding(file,meta) :
    ####cmp(binary data)
    global last_len
    global last_front_zero
    global last_b_int
    f = open(file,"rb")
    int_size = struct.calcsize('I')
    digit_data = ""
    while 1 :
        data = f.read(int_size)
        if data ==b'':
            break
        num = struct.unpack('I',data) #제발 대문자 i로 적어라 ㅠㅠㅠ          
        #print(num) #unpack 반환값 튜플임..
        s_num = list(num)
        #int 의 최대값: 2147483647
        #unsigned int의 최대값: 4294967295
        s_num = str(bin(s_num[0])) #다시 32자리 만들어줘야함
        #print(s_num) # 0b 포함되서 나옴
        s_num = s_num[2:]
        #print(s_num)  # 0b 끊기는거 확인됨.
        #0b10010100101110101011100100101010
        #11111011000100111110111101000000
        #두자리 차이나는것도 확인.
        c_num = s_num
        d_num = ""
        #print(s_num,",,,",len(s_num),"num: ",num[0])
        
        if ( len(s_num) == last_len - last_front_zero ) and (last_b_int == num[0]) :
            for i in range(last_front_zero) :
                d_num += "0"
            
        
        elif len(s_num) < 32 : #왜안되냐고...
            while 1 :
                s_num += "0"
                d_num += "0"
                if len(s_num) > 31 :
                    break
            

        complete_data = d_num + c_num
        #print(complete_data) 
        digit_data += complete_data
    #while문 끝나는부분
    #########################################
    f.close()
    
    #########meta dat
    m = open(meta,"rt")
    my_str = m.read()
    letter_binary = []
    cnt = 0
    pos = []
    #save pos
    for character in my_str :
        if character == '[' :
            pos.append(cnt)
        cnt += 1

    #letter_binary 만들자
    cnt = 0
    
    for idx in pos :
        letter_binary.append([])
        #문자
        if my_str[idx+2] == '\\' :
            letter_binary[cnt].append(my_str[idx+2:idx+4])
            if 'n' in letter_binary[cnt][0] :
                letter_binary[cnt][0] = '\n'
            else :
                letter_binary[cnt][0] = '\\'
        else :
            letter_binary[cnt].append(my_str[idx+2])
        #숫자
        if idx == pos[-1] :
            s_digit = ""
            for digit in my_str[pos[cnt]:-1] :
                if digit.isdigit() :
                    if digit == '0' or digit == '1' :
                        s_digit += digit
            letter_binary[cnt].append(s_digit)
            break
        else :
            s_digit = ""
            for digit in my_str[pos[cnt]:pos[cnt+1]] :
                if digit.isdigit() :
                    if digit == '0' or digit == '1' :
                        s_digit += digit
            letter_binary[cnt].append(s_digit)

        cnt += 1
    ##
    #print(letter_binary)
    #print(len(letter_binary))  #letter_binary가 메타데이터랑 일치함
    m.close()
    ##
    ##체크용 len (letter_binary[1])
    a = len(letter_binary[0][1])
    for letter in letter_binary :
        if a < len(letter[1]) :
            a = len(letter[1]) #a는 최대값

    
    #print()
    #print(digit_data)
    decoded_string = ""
    code = ""
    cnt = 0
    #####
    for digit in digit_data :
        code += digit
        pos = 0
        #체크
        '''
        if cnt == 1 :
            cnt += 1
            print("digit : ",digit)
            print("code : ",code)
        elif cnt == 2 :
            cnt += 1
            print("digit : ",digit)
            print("code : ",code)
        elif cnt == 3 :
            print("digit : ",digit)
            print("code : ",code)
            break
        if code == '100100' :
            print("digit : ",digit)
            print("code : ",code)
            cnt += 1
        ''' 
        ###
        for letter in letter_binary :
            #print(letter)
            #print(code)
            ''' # 문제없음 
            if len(letter) > 2 :
                print(letter)
                break
            '''
            if letter[1] == code :
                decoded_string += letter_binary[pos][0]
                #print(code)
                code = ""
                break
            #if len(code) == a :
                #print(code) #rtf 안되는이유 물어보기..!
            pos +=1
    #########
    
    #print(decoded_string)
    #print(code)
    #print(code)
    #print(digit_data) 문제없음
    ##원본텍스트 파일 만들기
    f = open(fname+"의 압축해제 결과.txt","wt")
    f.write(decoded_string)
    f.close()

fname = input("압축해제할 파일의 파일명을 확장자 없이 입력하세요 : ")
dname = fname
fname += ".cmp"
dname += ".dat"

decoding(fname,dname)
print()
print(" 압축해제가 완료되었습니다.\n 같은 폴더내의 Uncompressed Data.txt 파일을 확인하세요.")
print()



