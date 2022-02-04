#리스트 슬라이싱 제대로 쓰기

my_list = [1,'a',3,'b',5,'c',7,'d',8,'e',2,'f',1,'g',3,'h',4,'i',6,'j',7,'q']


nodes = []
while len(my_list) > 0 :
    print(my_list)
    nodes.append(my_list[0:2]) # 0~1 (2개씩) 끊어서 리스트로 만들어 리턴후 어펜드
    my_list = my_list[2:]
    

#리스트 컨캐쳐네이팅
nodes.sort()
newnode = []

cb_node1 = nodes[0][0] + nodes[1][0]  # 숫자 1+3 => 4
cb_node2 = nodes[0][1] + nodes[1][1]  # 문자 a+b => ab

newnode.append(cb_node1)
newnode.append(cb_node2)

newnodes = []

newnodes.append(newnode)
newnodes += nodes[2:]

## 재귀함수는 작업이 끝나면 종료되는 while(1) 문과 같음 (브레이크조건이 작업끝)
