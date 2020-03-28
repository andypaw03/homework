pole=[["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]

players=["X","0","A"]
ch=0
for i in pole:
    line =""
    for j in i:
        line +=j+"|"
    print(line[:-1])

while True:
    coord=int(input(f""))-1
    if pole[coord//5][coord%5]=="_":
        pole[coord//5][coord%5]=players[ch%3]
    else :
        print("Trololo, tobi ban. Try again")
        ch-=1

    for i in pole:
        line =" "
        for j in i:
            line += j + "|"
        print(line[:-1])
    ch+=1
    if pole[0][0]==pole[0][1]==pole[0][2]==pole[0][3]==pole[0][4] and pole[0][0]!="_":
        print("Great '_____' ",pole[0][0])
        break

    if pole[1][0]==pole[1][1]==pole[1][2]==pole[1][3]==pole[1][4] and pole[1][0]!="_":
        print("Great '_____' ",pole[1][0])
        break

    if pole[2][0]==pole[2][1]==pole[2][2]==pole[2][3]==pole[2][4] and pole[2][0]!="_":
        print("Great '_____' ",pole[2][0])
        break

    if pole[0][0]==pole[1][0]==pole[2][0]==pole[3][0]==pole[4][0] and pole[0][0]!="_":
        print("Great '_____' ",pole[0][0])
        break

    if pole[0][1]==pole[1][1]==pole[2][1]==pole[3][1]==pole[4][1]  and pole[0][1]!="_":
        print("Great '_____' ",pole[0][1])
        break

    if pole[0][2]==pole[1][2]==pole[2][2]==pole[3][2]==pole[4][2]  and pole[0][2]!="_":
        print("Great '_____' ",pole[0][2])
        break

    if pole[0][3]==pole[1][3]==pole[2][3]==pole[3][3]==pole[4][3] and pole[0][3]!="_":
        print("Great '_____' ",pole[0][3])
        break

    if pole[0][4]==pole[1][4]==pole[2][4]==pole[3][4]==pole[4][4] and pole[0][4]!="_":
        print("Great '_____' ",pole[0][4])
        break

    if pole[0][0]==pole[1][1]==pole[2][2]==pole[3][3]==pole[4][4]  and pole[0][0]!="_":
        print("Great '_____' ",pole[0][0])
        break

    if pole[0][4]==pole[1][3]==pole[2][2]==pole[3][1]==pole[4][0]  and pole[0][4]!="_":
        print("Great '_____' ",pole[0][4])
        break
