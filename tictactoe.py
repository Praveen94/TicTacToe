pos_list=[0,1,2,3,4,5,6,7,8]
playerA=True
playerB=False
playerAWon=False
playerBWon=False
chances=0
def insertPos(pos):
    global playerB
    global playerA
    global pos_list
    global chances
    if playerA:
        pos_list[pos]="A"
        chances+=1
        playerA=not playerA
        playerB=not playerB
    elif playerB:
        pos_list[pos]="B"
        chances+=1
        playerB=not playerB
        playerA=not playerA
    else:
        pass
def playerPos(name): # code for checking player has won
    global pos_list
    for i in range(3):
        if all(x==name for x in pos_list[3*i:(3*i)+3]): #checking all rows
            return name
        elif all(x==name for x in pos_list[i::3]): # checking all columns
            return name
        elif all(x==name for x in pos_list[i::4]): # checking ltr diagonal
            return name
        elif all(x==name for x in pos_list[i+2:7:2]): # checking rtl diagonal
            return name
        else:
            return None

def checkPlayer(): # code for checking if a player will win
    global playerAWon
    global playerBWon
    print("="*40)
    print(pos_list)
    playerAWon=playerPos("A")
    playerBWon=playerPos("B")
    if playerAWon=="A":
         return "A"

    elif playerBWon=="B":
        return "B"
    else:
        pass



while True:
    pos=int(input("Enter the position:"))
    if pos_list[pos-1]=="A" or pos_list[pos-1]=="B":
        continue
    insertPos(pos-1)
    if checkPlayer()=="A":
        print("Player A Won")
        break
    elif checkPlayer()=="B":
        print("Player B Won")
        break
else:
    print("Its a draw")
