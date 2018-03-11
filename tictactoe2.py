pos_list=["-","-","-","-","-","-","-","-","-"]
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
    print(pos_list[0]+" | "+pos_list[1]+" | "+pos_list[2])
    print("----------")
    print(pos_list[3]+" | "+pos_list[4]+" | "+pos_list[5])
    print("----------")
    print(pos_list[6]+" | "+pos_list[7]+" | "+pos_list[8])

def playerPos(name): # code for checking player has won
    global pos_list
    for i in range(3):

        if all(x==name for x in pos_list[3*i:(3*i)+3]): #checking all rows
            return name
        # elif all(x==name for x in pos_list[i::3]): # checking all columns
        #     return name

        elif ((pos_list[0]==pos_list[3]==pos_list[6]==name) or (pos_list[1]==pos_list[4]==pos_list[7]==name) or (pos_list[2]==pos_list[5]==pos_list[8]==name)):
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

    playerAWon=playerPos("A")
    playerBWon=playerPos("B")



    if playerAWon=="A":
        # print("PlayerAWon:{playerAWon}".format(playerAWon))
        return "A"

    elif playerBWon=="B":
        # print("PlayerBWon:{playerBWon}".format(playerBWon))
        return "B"
    else:
        print("PlayerAWon:"+str(playerAWon))
        print("PlayerBWon:"+str(playerBWon))
        # print("PlayerBWon:{playerBWon}".format(playerBWon))
        # print("PlayerAWon:{playerAWon}".format(playerAWon))
        pass



while True:
    pos=int(input("Enter the position:"))
    print()
    if pos not in range(1,10) or pos_list[pos-1]=="A" or pos_list[pos-1]=="B":
        print("\n")
        print("Please select another position.")
        continue
    insertPos(pos-1)
    print()
    if checkPlayer()=="A":
        print("Player A Won")
        break
    elif checkPlayer()=="B":
        print("Player B Won")
        break
    else:
        pass
    if chances==9:
        print("Its a draw")
        break