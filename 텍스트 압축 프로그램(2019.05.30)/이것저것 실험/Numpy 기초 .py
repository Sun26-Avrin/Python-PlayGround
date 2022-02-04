# 빈도수 세기 함수 
def letter_frequency(line) :
    line.lower()
    global my_dic
    
    my_dic['a'] += line.count('a')
    my_dic['b'] += line.count('b')
    my_dic['c'] += line.count('c')
    my_dic['d'] += line.count('d')
    my_dic['e'] += line.count('e')
    my_dic['f'] += line.count('f')
    my_dic['g'] += line.count('g')
    my_dic['h'] += line.count('h')
    my_dic['i'] += line.count('i')
    my_dic['j'] += line.count('j')
    my_dic['k'] += line.count('k')
    my_dic['l'] += line.count('l')
    my_dic['m'] += line.count('m')
    my_dic['n'] += line.count('n')
    my_dic['o'] += line.count('o')
    my_dic['p'] += line.count('p')
    my_dic['q'] += line.count('q')
    my_dic['r'] += line.count('r')
    my_dic['s'] += line.count('s')
    my_dic['t'] += line.count('t')
    my_dic['u'] += line.count('u')
    my_dic['v'] += line.count('v')
    my_dic['w'] += line.count('w')
    my_dic['x'] += line.count('x')
    my_dic['y'] += line.count('y')
    my_dic['z'] += line.count('z')

## 알파벳 빈도수 초기화
my_dic = dict(zip(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                  ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ))

# 정렬된 딕셔너리
my_dic2 = {}
# 빈도수에 따라 2진수로 바뀐 딕셔너리
my_dic3 = {}
    

# 빈도수 높은 것 찾기
def define_num() :
    global my_dic
    s_dic = sorted(my_dic.items(), key=lambda x:x[1],reverse=True)
    global my_dic2
    my_dic2 = dict(s_dic)
    
    global my_dic3
    my_dic3 = dict(s_dic)
    bin_num = 0b0
    for i in my_dic3 :
        my_dic3[i] = bin_num
        bin_num += 0b1
        
###메인###########   
    

file = open('Release\input_alice.rtf','r')

while 1 :
    str1 = file.readline()
    if not str1 : break
    letter_frequency(str1)
    #print(str1.count('a'))

define_num()


file.close()


#### 메타데이터 만들기###
def metadata() :
    global my_dic3
    file = open('metadata.dat','wt')
    
    file.write(str(my_dic3))
    file.close()


metadata()

#### 압축파일 만들기 ####
import struct

def encoding() :
    global my_dic3
    file = open('Release\input_alice.rtf','r')
    encode = open('metadata.bin','ab+') # 생성 & 추가
    
    while 1 :
        str1 = file.readline()
        bin1 = 0b0
        if not str1 : break
        #print(str1)
        for vocab in str1 :
            #print(vocab)
            if vocab.isalpha() :
                vocab = vocab.lower()
                bin1 = my_dic3[vocab]
                data = struct.pack('i',bin1)
                encode.write(data)
            else :
                bin1 = vocab
                data = bin1.encode('utf-8')
                
                encode.write(data)

    file.close()
    encode.close()

encoding()
