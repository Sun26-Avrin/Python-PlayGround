#int 최대값을 넣었을때 bin 을 쓰면 어떻게될까

u_int = 4294967295 #unsigned int 의 최대값.

a = bin(u_int)

u_int += 1

b = bin(u_int)

