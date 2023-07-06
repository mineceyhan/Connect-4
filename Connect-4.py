
import random
from sys import exit

print("\n        Welcome to Connect Four")
print("---------------------------------------------")


gameBoard = [["","","","","","","","",""], 
             ["","","","","","","","",""], 
             ["","","","","","","","",""], 
             ["","","","","","","","",""], 
             ["","","","","","","","",""],
             ["","","","","","","","",""],
             ["","","","","","","","",""],
             ["","","","","","","","",""],
             ["","","","","","","","",""]]

rows = 9
cols = 9

player = ["" ,""]

def choisePlayerStart():
    mylist = ["A", "B"]
    choice = random.choice(mylist);
    player[0] =choice
    for i  in mylist:
        if i!=choice :
            player[1] =i

def printGameBoard():
    print("\n     0    1    2    3    4    5    6    7    8  ", end="")
    for x in range(rows):
      print("\n   +----+----+----+----+----+----+----+----+----+")
      print(x, " |", end="")
      for y in range(cols):
        if(gameBoard[x][y] == "🔵"):
          print("",gameBoard[x][y], end=" |")
        elif(gameBoard[x][y] == "🔴"):
          print("", gameBoard[x][y], end=" |")
        else:
          print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+----+----+")

def restart():
    for x in range(rows):
      for y in range(cols):
          gameBoard[x][y] = "";
    choisePlayerStart()
    firstWriteBoardFile()
    cleanMoveFile()
    game()
    
def continueGame():
    choisePlayerStart()
    slot = []
    color =[]
    with open("Tahta.txt", mode="r") as f:  
        veri = f.readlines()
        for i in range(rows*cols):
            x = veri[i].split(":")
            slot.append(x[0]) 
            color.append(x[1])
    count =0
    for x in range(rows):
      for y in range(cols):
          count+=1
          if(count!=81):
              if(color[count][0] == player[0]):
                  modifyArray(slot[count], '🔵')
                  print(slot[count][0] ,color[count][0])
              elif(color[count][0] == player[1]):
                  modifyArray(slot[count], '🔴')
                  print(slot[count],color[count][0])         
    printGameBoard()
    

def modifyArray(spacePicked, turn):
    if(type(spacePicked) == str ): 
        gameBoard[int(spacePicked[0])][int(spacePicked[1])] = turn
    else:
        gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
  #YATAY
  for y in range(rows):
    for x in range(cols - 3):
      if gameBoard[x][y] == chip and gameBoard[x+1][y] == chip and gameBoard[x+2][y] == chip and gameBoard[x+3][y] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  # DİKEY
  for x in range(rows):
    for y in range(cols - 3):
      if gameBoard[x][y] == chip and gameBoard[x][y+1] == chip and gameBoard[x][y+2] == chip and gameBoard[x][y+3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  # Sağ üstten sol alta çapraz
  for x in range(rows - 3):
    for y in range(3, cols):
      if gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  # Sol üstten sağ alta çapraz
  for x in range(rows - 3):
    for y in range(cols - 3):
      if gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True
  return False

def coordinateParser(inputString):
    if(len(inputString) ==2):
        try:
            coordinate = [None] * 2
            coordinate[0] = int(inputString[0])
            coordinate[1] = int(inputString[1])
            return coordinate
        except:
            print("Not a valid coordinate")
    else:
        print("Not a valid coordinate")

def isSpaceAvailable(intendedCoordinate):
  if(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴'):
    return False
  elif(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵'):
    return False
  else:
    return True

def gravityChecker(intendedCoordinate):
  ### Calculate space below
  spaceBelow = [None] * 2
  spaceBelow[0] = intendedCoordinate[0] + 1 # girilen satırın altındaki alan
  spaceBelow[1] = intendedCoordinate[1]
  ### ground level ?
  if(spaceBelow[0] == 9):
    return True
  ### Check slot
  if(isSpaceAvailable(spaceBelow) == False):
    return True
  return False

################## DOSYA İSLEMLERİ ##################
# Hamle.txt
def writeMoveFile(player,coordinate): 
    try:
        with open("Hamle.txt", mode="a") as f: # read and write ,varolan verileri silmez
            f.write(player)
            f.write(":")
            f.write(str(coordinate[0]))
            f.write(str(coordinate[1]))
            f.write("\n")
    except:
        print("File Error!")

def cleanMoveFile():
    try:
        with open("Hamle.txt", mode="w") as f:
            f.truncate()
    except:
        print("File Error!")

# Tahta.txt 
def firstWriteBoardFile():
    try:
        with open("Tahta.txt", mode="w") as f:
            for i in range(rows):
                for j in range(cols):
                    f.write(str(i))
                    f.write(str(j))
                    f.write(":0")
                    f.write("\n")
    except:
        print("File Error!")

def UpdateWriteBoardFile(coordinate ,player):
    slot_coordinate = str(coordinate[0])+str(coordinate[1])
    with open("Tahta.txt", mode="r+") as f:
        veri = f.readlines()
        for i in range(rows*cols):
            x = veri[i].split(":")
            if slot_coordinate==x[0]:
                x[1] = player
                veri[i] =str(x[0])+ ":" + str(x[1]) +"\n"
                break
        f.seek(0)
        f.truncate()        # dosya içindeki verileri sil
        f.writelines(veri)  # dosyaya yeni verileri yaz

######################################################

def game():
    leaveLoop = False
    turnCounter = 0
    tieCount1 = 0
    tieCount2 =  0
    while(leaveLoop == False):
        printGameBoard()
        #Player 1
        if(turnCounter % 2 == 0):
            while True:
                print("\nPLAYER " + player[0] + " :")
                spacePicked = input("Press 0 for Exit\n or Choose a space: ")
                if(spacePicked == "0"):
                    ch = input("Press 1 Continue \n Press 2 Restart: ")
                    if(ch == "1"):
                        continueGame()
                    elif(ch =="2"):
                        restart()
                else:
                    coordinate = coordinateParser(spacePicked)
                    try:
                        # seçilen slot uygun mu?
                        if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
                            modifyArray(coordinate, '🔵')
                            writeMoveFile(player[0], coordinate)
                            UpdateWriteBoardFile(coordinate ,player[0])
                            tieCount1 +=1
                            break
                        else:
                            print("Not a valid coordinate")
                    except:
                        print("Error occured. Please try again.")
            winner = checkForWinner('🔵')
            turnCounter += 1
            print(tieCount1)
        #Player 2
        else:
            while True:
               print("\nPLAYER " + player[1] + " :")
               spacePicked = input("Press 0 for Exit\n or Choose a space: ")
               # exit game
               if(spacePicked == "0"):
                ch = input("Press 1 Continue \n Press 2 Restart: ")
                if(ch == "1"):
                    continueGame()
                elif(ch =="2"):
                    restart()
               else:
                   coordinate = coordinateParser(spacePicked)
                   try:
                       # seçilen slot uygun mu?
                       if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
                           modifyArray(coordinate, '🔴')
                           tieCount2 += 1
                           writeMoveFile(player[1], coordinate)
                           UpdateWriteBoardFile(coordinate ,player[1])
                           break
                       else:
                           print("Not a valid coordinate")
                   except:
                       print("Error occured. Please try again.")
            winner = checkForWinner('🔴')
            turnCounter += 1
            print(tieCount2)
        if(winner):
          printGameBoard()
          ch = input("Press 1 Exit \n Press 2 Restart: ")
          if(ch == "1"):
             exit()
          elif(ch =="2"):
              restart()
          break
        if(tieCount1 == 40 and tieCount2 == 40):
             print("TIE")
             ch = input("Press 1 Exit \n Press 2 Restart: ")
             if(ch == "1"):
                exit()
             elif(ch =="2"):
                 restart()

    

choisePlayerStart()
firstWriteBoardFile()
cleanMoveFile()
game()



