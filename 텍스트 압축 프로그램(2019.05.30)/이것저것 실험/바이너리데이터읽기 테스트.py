import struct

f = open("input_alice.cmp","rb")
intsize = struct.calcsize('i')
while 1 :
    data = f.read(intsize)
    if data == b'':
        break



    
    num = struct.unpack('I',data)
    s_num = list(num)
    binary = str(bin(s_num[0]))
    binary = binary[2:]
    

