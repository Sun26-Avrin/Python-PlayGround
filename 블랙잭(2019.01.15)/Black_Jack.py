#클래스 -------------------------------------------------------------------------
# 플레이어 클래스
class Account :
    # 사용법 1.[세팅] Set()  2.[베팅] Bet(a)
             #-> [게임끝] 2. Cal() 3. 승리,무승부 선언(Win(),Draw())
    def __init__(self, ID, Coin) :
        self.Account = ID
        self.Coin = Coin
    def Set(self) :
        self.S_list =[]
        self.Sum = 0
    def balance(self) :
        return self.Coin
    def Bet(self, bet) :
        self.bet = bet
        self.S_list.append(bet)
        self.Coin =self.Coin - bet
    def Cal(self) :
        if len(self.S_list) == 4 :
            self.Sum = 150
        elif len(self.S_list) == 3:
            self.Sum = 70
        elif len(self.S_list) == 2:
            self.Sum = 30
        else :
            self.Sum = 10
    def Win(self):
        self.Coin = self.Coin + self.Sum*2
    def Draw(self):
        self.Coin = self.Coin + self.Sum

# 딜러 클래스
class Dealer_Account (Account) :
    def Cal(self) :
        self.Sum = 50*len(self.S_list)
    def Win(self) :
        self.Coin = self.Coin + self.Sum
#클래스------------------------------------------------------------------------
#세팅--------------------------------------------------------------------
P = Account(input("ID를 입력하세요: "), int(input("시작 코인은 얼마입니까?: ")))
D = Dealer_Account("Dealer", 500)

import turtle

t=turtle.Turtle()

t.hideturtle()
t.speed(10)
t.penup()

import random

#카드뽑기 함수---------------------------------------------------------------------
def Drawcards(x, y):
    t.penup()
    t.setheading(180)
    t.goto(x-80,y+100)           #x=k, y=200
    t.right(180)
    t.pendown()
    
    for i in range(4) :
        if i==0 or i==2 :
            t.forward(100)
            t.right(90)
        if i==1 or i==3 :
            t.forward(150)
            t.right(90)

    #1. 클로버, 다이아 뽑기
    Shape = random.randrange(0,2)
    #2. 클로버, 다이아 중 1개뽑기
    Number = random.randrange(0,len(cards[Shape]))
    #3. 카드 인식
    recogN = cards[Shape][Number][0]
    #5. 삭제
    cards[Shape].pop(Number)
    t.penup()
    # 카드 숫자
    if recogN == "A" :
        t.goto(x+10,y+80)
        t.write("A", font=(10))
        t.goto(x-75,y-45)
        t.write("A", font=(10))
    elif recogN == "J" :
        t.goto(x+10,y+80)
        t.write("J", font=(10))
        t.goto(x-75,y-45)
        t.write("J", font=(10))
    elif recogN == "Q" :
        t.goto(x+5,y+80)
        t.write("Q", font=(10))
        t.goto(x-75,y-45)
        t.write("Q", font=(10))
    elif recogN == "K" :
        t.goto(x+10,y+80)
        t.write("K", font=(10))
        t.goto(x-75,y-45)
        t.write("K", font=(10))
    elif recogN == "T" :
        t.goto(x+0,y+80)
        t.write("10", font=(10))
        t.goto(x-75,y-45)
        t.write("10", font=(10))
        
            
    else :
        t.goto(x+10,y+80)
        t.write(recogN, font=(10))
        t.goto(x-75,y-45)
        t.write(recogN, font=(10))
    

    #클로버
    if Shape == 0 :
        #-30 #+30
        t.goto(x-40,y+30)
        t.dot(25)
        t.goto(x-20,y+30)
        t.dot(25)
        t.goto(x-30,y+45)
        t.dot(25)
        t.goto(x-30,y+30)
        t.setheading(180)
        t.begin_fill()
        t.circle(20, steps=3)
        t.end_fill()      

    #다이아
    if Shape == 1 :
        t.color("red")
        t.goto(x-30,y+60)
        t.setheading(180)
        t.begin_fill()
        t.circle(20, steps=3)
        t.end_fill()
        t.goto(x-30,y+0)
        t.setheading(0)
        t.begin_fill()
        t.circle(20, steps=3)
        t.end_fill()
        t.color("black")
    #리턴값
    if recogN == "A" :
        if y>0:
            return "D", 11
        else :
            return "P", 11
    elif recogN == "J" or recogN == "Q" or recogN == "K" or recogN == "T" :
        if y>0:
            return "D", 10
        else :
            return "P", 10
    else :
        if y>0:
            return "D", int(recogN)
        else:
            return "P", int(recogN)
#------------------------------------------------------------------------------------

#Game Start!

End = 0
#Game Start!
while P.Coin > 0 and End != "yes" :
    cards = [
     ["A클로버", "2클로버", "3클로버", "4클로버", "5클로버", "6클로버", "7클로버", "8클로버", "9클로버", "T클로버", "J클로버", "Q클로버", "K클로버"],
     ["A다이아", "2다이아", "3다이아", "4다이아", "5다이아", "6다이아", "7다이아", "8다이아", "9다이아", "T다이아", "J다이아", "Q다이아", "K다이아"]
    ]
    # 초기화
    P.Set()
    D.Set()
    Dealer_Card = []
    Player_Card = []

    # ID & Coin
    t.hideturtle()
    t.speed(10)
    t.penup()
    t.goto(300,300)
    t.write(P.Account, font=(30))
    t.goto(300,280)
    t.write(P.Coin, font=(28))
    t.goto(300,0)
    t.color("blue")
    t.write("게임끝내기 : 'yes' \n카드받기 : 'hit'\nStop : 'stand'",font=(20))
    t.color("black")
    
    # 카드 분배
    for i in range(4) :
        # 딜러 2장 
        if i<2 :
            #4. 함수 호출 
            Dealer_Card.append(Drawcards(-330+110*i,200)[1])
        # 플레이어 2장 
        else :
            #4. 함수 호출
            Player_Card.append(Drawcards(-330+110*(i-2),-200)[1])

    Dealer_Card.sort()
    Player_Card.sort()
    #--------------------------------------------------------------------------------
    # 배팅 코인
    # 플레이어 배팅
    P.Bet(10)
    # 배팅된 금액
    t.goto(280,-280)
    t.write("배팅 금액",font=(20))
    t.goto(280,-300)
    t.write(P.bet, font=(20))       


    # 점수

    Dealer_Score = Dealer_Card[0]+Dealer_Card[1]
    if Dealer_Score > 21:
        Dealer_Card.sort()
        Dealer_Card[-1] = 1
        Dealer_Score = Dealer_Score - 10
    Player_Score = Player_Card[0] + Player_Card[1]
            
    i=-1
    k=-1

    # Hit
    while 1 :        
        Answer = input("카드를 한장 더 받으시겠습니까? ")
        Answer = Answer.lower()
        if Answer == 'hit':
            # 5장 초과제한
            if len(Player_Card) == 5 :
                break
            P.Bet(10*2**(i+2))
            t.goto(280+30*(i+1)+19,-300)
            t.write("+", font=(15)) 
            t.goto(280+30*(i+2),-300)
            t.write(P.bet, font=(20))
            
            i=i+1 #i=0
            #4. 함수 호출 + 점수변환
            Player_Card.append(Drawcards(-330+110*(i+2),-200)[1])
            Player_Score = Player_Score + Player_Card[i+2]
            Player_Card.sort()
            if Player_Score > 21 and Player_Card[-1] == 11 :
                Player_Card[-1] = 1
                Player_Score = Player_Score - 10
            elif Player_Score > 21 and Player_Card[-1] != 11 :
                break
            elif Player_Score == 21 :
                break
# 딜러 AI ---------------------------------------------------------------------------------------            
        elif Answer == 'stand' :#딜러턴 
            if Dealer_Score > Player_Score :
                break
            #확률 계산 
            def Sun() :
                global pre
                global pre2
                global pre3
                global pre4
                Clo_List =[]
                Dia_List =[]
                for c in range(len(cards[0])):
                    RecogN = cards[0][c][0]            
                    if RecogN == "A" :
                        RecogN = 11
                    elif RecogN == "J" or RecogN == "Q" or RecogN == "K" or RecogN == "T" :
                        RecogN = 10
                    else :
                        RecogN = int(RecogN)
                    Clo_List.append(RecogN)
                    
                        
                for c in range(len(cards[1])) :
                    RecogN = cards[1][c][0]
                    if RecogN == "A" :
                        RecogN = 11
                    elif RecogN == "J" or RecogN == "Q" or RecogN == "K" or RecogN == "T" :
                        RecogN = 10
                    else :
                        RecogN = int(RecogN)
                    Dia_List.append(RecogN)
                    
                    
                #초기화
                Clo_List.sort()
                Dia_List.sort()
                #클로버 경우의수 
                for c in range(len(Clo_List)) :
                    D_Csum = Dealer_Score + Clo_List[c]
                    # 초기화
                    Check1 = 0
                    Check2 = [1]
                    # A 바꾸기
                    import copy
                    if D_Csum >21 and (Clo_List[c] == 11 or Dealer_Card[-1] == 11) :
                        D_Csum = D_Csum - 10
                    if D_Csum > 21 and (Dealer_Card[-1] != 11 and Clo_List[c] == 11) :
                        Check1 = 1
                    if D_Csum > 21 and Dealer_Card[-1] == 11 :
                        Check2 = copy.deepcopy(Dealer_Card)
                        Check2[-1] = 0 #Check2 는 리스트
                    
                    # 삭제 & 잠재적 두번째 합 // 두번째 반복문
                    N = Clo_List.pop(c)
                    for Pie in range(len(Clo_List)) :
                        D_Csum1 = D_Csum + Clo_List[Pie]
                        # A 바꾸기
                        if D_Csum1 >21 and (Clo_List[Pie] == 11 or (N == 11 and Check1 != 1 ) or (Check2[-1] != 0 and Dealer_Card[-1] == 11) ) :
                            D_Csum1 = D_Csum1 - 10

                        # 경우의 수 
                        if D_Csum <= 21 and D_Csum1 <= 21 and Dealer_Score <= 11 and D_Csum1 >= Player_Score :
                            pre.append(1)
                        elif D_Csum <= 21 and D_Csum1 <= 21 and Dealer_Score > 11 and D_Csum >= Player_Score :
                            pre.append(1)
                        else :
                            pre2.append(1)
                    # 본 반복문
                    if D_Csum <= 21 and D_Csum >= Player_Score :
                        pre3.append(1)
                    else :
                        pre4.append(1)
                    # 초기화
                    Clo_List.append(N)
                    Clo_List.sort()
                    
                #다이아 경우의 수    
                for c in range(len(Dia_List)):
                    D_Dsum = Dealer_Score + Dia_List[c]
                    #초기화
                    Check1 = 0
                    Check2 = [1]
                    # A 바꾸기
                    import copy
                    if D_Dsum >21 and (Dia_List[c] == 11 or Dealer_Card[-1] == 11) :
                        D_Dsum = D_Dsum - 10
                    if D_Dsum > 21 and (Dealer_Card[-1] != 11 and Dia_List[c] == 11) :
                        Check1 = 1
                    if D_Dsum > 21 and Dealer_Card[-1] == 11 :
                        Check2 = copy.deepcopy(Dealer_Card)
                        Check2[-1] = 0 #Check2 는 리스트
                    
                    # 삭제 & 잠재적 두번째 합 // 두번째 반복문
                    N = Dia_List.pop(c)
                    for Pie in range(len(Dia_List)) :
                        D_Dsum1 = D_Dsum + Dia_List[Pie]
                        # A 바꾸기
                        if D_Dsum1 >21 and (Dia_List[Pie] == 11 or (N == 11 and Check1 != 1 ) or (Check2[-1] != 0 and Dealer_Card[-1] == 11) ) :
                            D_Dsum1 = D_Dsum1 - 10
                    
                        # 경우의 수
                        
                        if D_Dsum <= 21 and D_Dsum1 <= 21 and Dealer_Score <= 11 and D_Dsum1 >= Player_Score :
                            pre.append(1)
                        elif D_Dsum <= 21 and D_Dsum1 <= 21 and Dealer_Score > 11 and D_Dsum >= Player_Score :
                            pre.append(1)
                        else :
                            pre2.append(1)
                        
                    # 본 반복문         
                    if D_Dsum <= 21 and D_Dsum >= Player_Score :
                        pre3.append(1)
                    else :
                        pre4.append(1)
                    # 초기화    
                    Dia_List.append(N)
                    Dia_List.sort()
                    
                
                #print(len(pre))
                #print(len(pre2))
                #print(len(pre3))
                #print(len(pre4))
            #딜러 카드 받기 -------------------------------------------
            while 1 :
                c=0
                pre=[] # win
                pre2=[]# Lose
                pre3=[]# win
                pre4=[]# Lose
                Sun()
                if (len(pre) > len(pre2) and Player_Score < 21) or (len(pre3) > len(pre4) and Player_Score < 21) :
                    if len(Dealer_Card) == 5:
                        break
                    D.Bet(50)
                    #딜러배팅액 표기
                    k=k+1 #k=0
                    #딜러 카드 호출
                    Dealer_Card.append(Drawcards(-330+110*(k+2),200)[1])
                    Dealer_Score = Dealer_Score + Dealer_Card[k+2]
                    Dealer_Card.sort()
                    if Dealer_Score >21 and Dealer_Card[-1] == 11 :
                        Dealer_Card[-1] = 1
                        Dealer_Score = Dealer_Score - 10
                    elif Dealer_Score > 21 and Dealer_Card[-1] != 11:
                        break
                    elif Dealer_Score == 21 :
                        break
                else :
                    break
            break
        else :
            continue

    # 게임결과 & 코인차감  
    while 1 :
        if Player_Score > 21 or (Player_Score < 22 and Player_Score < Dealer_Score) :
            print("Player Lose")
            D.Cal()
            D.Win()
            break
        elif Player_Score < 22 and Player_Score > Dealer_Score :
            print("Player Win")
            P.Cal()
            P.Win()
            break
        elif Player_Score < 22 and Player_Score == Dealer_Score :
            print("Draw")
            D.Cal()
            D.Draw()
            P.Cal()
            P.Draw()
            break

    End = input("게임을 끝내시겠습니까? ")
    End.lower()
    t.reset()

t.hideturtle()
