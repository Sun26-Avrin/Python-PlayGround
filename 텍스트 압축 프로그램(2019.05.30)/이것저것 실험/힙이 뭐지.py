#힙은 데이터에서 최대(최소)를 빠르게 찾을 수 있는 자료구조
#힙은 완전이진트리
#우선순위 큐 : 입력순서에 상관없이 우선순위가 높은 데이터가 가장먼저 처리됨


import heapq #리스트를 min heap처럼 사용가능하게함
import struct


#최소힙(min heap) : 가장 작은값이 루트에 위치 (모든 부모노드는 자식보다 작거나 같다)
'''
#method
self.heappush(원소추가할대상리스트,추가할원소)   #O(logN) 시간복잡도
'''
def pow_SIGMA(i) : # k는 1부터 i 까지
    my_sum = 0
    for k in range(1,i+1,1) :
        my_sum += 2**k
    return my_sum


class HeapNode :
    def __init__(self,char,count) :
        self.char = char
        self.count = count
        self.left = None
        self.right = None


class Encoding :  # Encoding(file_name) 형태로 호출하기.
    def __init__(self,file_name) :
        self.heap = [] #최대힙 저장 (-count, count, key)  인덱스 [1] 이 최대힙
        self.count = {} #문자 갯수(빈도수)
        self.file_name = file_name
        self.digit = {} #바이너리데이터 저장!!!!
        self.tree = [] #완전이진트리 (문자로구성됨) max_heap
    
    def make_count(self,text) :
        
        for ch in text :
            if not ch in self.count :
                self.count[ch] = 0
            self.count[ch] += 1


    def make_heap(self) :
        for key in self.count : #딕셔너리의 키 값을 순회
            heapq.heappush(self.heap, (-self.count[key],self.count[key], key) ) #리스트에 힙노드클래스 추가

    def make_tree(self) : #트리만들필요없음....
        for heap in self.heap :
            self.tree.append(heap[2]) 

    def make_digit(self) :
        l_bindata = 0b0
        r_bindata = 0b1
        #########
        #p = 0                       ## ( [0] ), ( 1,2 ) [1],( 3,4 [2],5,6 ) [3],7,8
        level = 0                    ## 2**k
        index = 0
        cnt = 4
        z_cnt = 3
        for heap in self.heap :
            if level == 0 :
                self.digit[heap[2]] = "{0:b}".format(0).zfill(1)
                level += 1
            elif level == 1 :
                self.digit[heap[2]] = "{0:b}".format(0).zfill(2)
                self.digit[heap[2]] = "{0:b}".format(1).zfill(2)
            else :
                if ( index == (   2**level + pow_SIGMA(level-1)    )    ) :
                    for i in range(cnt) :
                        self.digit[heap[2]] = "{0:b}".format(1).zfill(z_cnt)


                    zcnt+= 1
                    cnt *= 2
                

            index += 1
            
            
        
            
                





            k += 1
        
        
    

    def make_text(self) :        
        

A = Encoding()
text = "abcdefggaaf"
A.make_count(text)
A.make_heap()


