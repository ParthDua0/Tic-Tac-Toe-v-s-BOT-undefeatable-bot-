a={1:'-',2:' ',3:'-',4:' ',5:'_',6:' ',7:'-',8:' ',9:'-'}
_format_=' 1 | 2 | 3 \n ---+---+---\n  4 | 5 | 6 \n ---+---+---\n  7 | 8 | 9 '
player_1=input('Enter your name (player 1 | X) : ')
player_2='Mr.Bot'
print(a[1], '|', a[2], '|', a[3])
print('--+---+--')
print(a[4], '|', a[5], '|', a[6])
print('--+---+--')
print(a[7], '|', a[8], '|', a[9])
print('\n',_format_)
a2=0
while True:
    if a[1]==a[2]==a[3] or a[4]==a[5]==a[6] or a[7]==a[8]==a[9] or a[1]==a[4]==a[7] or a[2]==a[5]==a[8] or a[3]==a[6]==a[9] or a[1]==a[5]==a[9] or a[3]==a[5]==a[7]:
        print(str(player_2)+' Won')
        break
    a2+=1
    b=int(input('Enter your choice '+str(player_1)+' [X] : '))
    while b>9 or b<1 or a[b]=='X' or a[b] =='O':
        print('please enter a valid value....')
        b=int(input('Enter your choice '+str(player_1)+' [X] : '))
        if b>9 or b<1 or a[b]=='X' or a[b] =='O':
            continue
        break
    a[b]='X'
    print(a[1], '|', a[2], '|', a[3])
    print('--+---+--')
    print(a[4], '|', a[5], '|', a[6])
    print('--+---+--')
    print(a[7], '|', a[8], '|', a[9])
    print('\n',_format_)
    if a[1]==a[2]==a[3] or a[4]==a[5]==a[6] or a[7]==a[8]==a[9] or a[1]==a[4]==a[7] or a[2]==a[5]==a[8] or a[3]==a[6]==a[9] or a[1]==a[5]==a[9] or a[3]==a[5]==a[7]:
        print(str(player_1)+' Won')
        break
    if a2==5:
        print('DRAW....')
        break
    if a2==1:
        if b != 5:
            c=5
            b1=b
        else:
            c=1
            b1=b
    elif a2==2:
        if b1==1:
            if b in (6,8):
                c=9
            elif b==7:
                c=4
            elif b==9:
                c=8
            elif b==2:
                c=3
            elif b==4:
                c=7
            elif b==3:
                c=2
        elif b1==2:
            if b in (7,8,9):
                c=6
            elif b==1 or b==6:
                c=3
            elif b==3 or b==4:
                c=1
        elif b1==3:
            if b in (4,8):
                c=7
            elif b==1:
                c=2
            elif b==2:
                c=1
            elif b==6:
                c=9
            elif b==7:
                c=8
            elif b==9:
                c=6
        elif b1==4:
            if b in (3,6,9):
                c=2
            elif b==1 or b==8:
                c=7
            elif b==2 or b==7:
                c=1
        elif b1==5:
            if b==2:
                c=8
            elif b==3:
                c=7
            elif b==4:
                c=6
            elif b==6:
                c=4
            elif b==7:
                c=3
            elif b==8:
                c=2
            elif b==9:
                c=7
        elif b1==6:
            if b in (1,4,7):
                c=8
            elif b==3 or b==8:
                c=9
            elif b==2 or b==9:
                c=3
        elif b1==7:
            if b in (2,6):
                c=3
            elif b==9:
                c=8
            elif b==8:
                c=9
            elif b==1:
                c=4
            elif b==4:
                c=1
            elif b==3:
                c=2
        elif b1==8:
            if b in (1,2,3):
                c=4
            elif b==4 or b==9:
                c=7
            elif b==6 or b==7:
                c=9
        elif b1==9:
            if b in (2,4):
                c=1
            elif b==7:
                c=8
            elif b==8:
                c=7
            elif b==3:
                c=6
            elif b==6:
                c=3
            elif b==1:
                c=4
        b2=b
    elif a2==3:
        if b1==1:
            if b2==6:
                if b==2:
                    c=3
                elif b==3:
                    c=2
                elif b==4:
                    c=7
                elif b==7:
                    c=4
                elif b==8:
                    c=7
            elif b2==8:
                if b==2:
                    c=3
                elif b==3:
                    c=2
                elif b==4:
                    c=7
                elif b==7:
                    c=4
                elif b==6:
                    c=3
            elif b2==2:
                if b in (4,6,8,9):
                    c=7
                elif b==7:
                    c=4
            elif b2==3:
                if b in (4,6,7,9):
                    c=8
                elif b==8:
                    c=4
            elif b2==4:
                if b in (2,6,8,9):
                    c=3
                elif b==3:
                    c=2
            elif b2==7:
                if b in (2,3,8,9):
                    c=6
                elif b==6:
                    c=8
            elif b2==9:
                if b in (3,4,6,7):
                    c=2
                elif b==2:
                    c=3
        elif b1==2:
            if b2==7:
                if b in (1,3,8,9):
                    c=4
                elif b==4:
                    c=1
            elif b2==8:
                if b in (1,3,7,9):
                    c=4
                elif b==4:
                    c=9
            elif b2==9:
                if b in (1,3,7,8):
                    c=4
                elif b==4:
                    c=7
            elif b2==1:
                if b in (4,6,8,9):
                    c=7
                elif b==7:
                    c=4
            elif b2==6:
                if b in (1,4,8,9):
                    c=7
                elif b==7:
                    c=9
            elif b2==3:
                if b in (4,6,7,8):
                    c=9
                elif b==9:
                    c=6
            elif b2==4:
                if b in (3,4,7,8):
                    c=9
                elif b==9:
                    c=3
        elif b1==3:
            if b2==4:
                if b==1:
                    c=2
                elif b==2:
                    c=1
                elif b==6:
                    c=9
                elif b==8:
                    c=9
                elif b==9:
                    c=6
            elif b2==8:
                if b==1:
                    c=2
                elif b==2:
                    c=1
                elif b==4:
                    c=1
                elif b==6:
                    c=9
                elif b==9:
                    c=6
            elif b2==1:
                if b in (4,6,7,9):
                    c=8
                elif b==8:
                    c=4
            elif b2==2:
                if b in (4,6,7,8):
                    c=9
                elif b==9:
                    c=6
            elif b2==6:
                if b in (2,4,7,8):
                    c=1
                elif b==1:
                    c=2
            elif b2==7:
                if b in (1,4,6,9):
                    c=2
                elif b==2:
                    c=1
            elif b2==9:
                if b in (1,2,7,8):
                    c=4
                elif b==4:
                    c=8
        elif b1==4:
            if b2==3:
                if b in (1,6,7,9):
                    c=8
                elif b==8:
                    c=7
            elif b2==9:
                if b in (1,3,6,7):
                    c=8
                elif b==8:
                    c=7
            elif b2==6:
                if b in (1,3,7,9):
                    c=8
                elif b==8:
                    c=3
            elif b2==1:
                if b in (2,6,8,9):
                    c=3
                elif b==3:
                    c=2
            elif b2==8:
                if b in (1,2,6,9):
                    c=3
                elif b==3:
                    c=1
            elif b2==2:
                if b in (3,6,7,8):
                    c=9
                elif b==9:
                    c=3
            elif b2==7:
                if b in (2,3,6,8):
                    c=9
                elif b==9:
                    c=8
        elif b1==5:
            if b2==2:
                if b==3:
                    c=7
                elif b==4:
                    c=6
                elif b==6:
                    c=4
                elif b==7:
                    c=3
                elif b==9:
                    c=7
            elif b2==3:
                if b in (2,6,8,9):
                    c=4
                elif b==4:
                    c=6
            elif b2==4:
                if b==2:
                    c=8
                elif b==3:
                    c=7
                elif b==7:
                    c=3
                elif b==8:
                    c=2
                elif b==9:
                    c=3
            elif b2==6:
                if b in (2,3,8,9):
                    c=7
                elif b==7:
                    c=3
            elif b2==7:
                if b in (4,6,8,9):
                    c=2
                elif b==2:
                    c=8
            elif b2==8:
                if b in (4,6,7,9):
                    c=3
                elif b==3:
                    c=7
            elif b2==9:
                if b in (2,3,6,8):
                    c=4
                elif b==4:
                    c=6
        elif b1==6:
            if b2==1:
                if b in (3,4,7,9):
                    c=2
                elif b==2:
                    c=3
            elif b2==4:
                if b in (1,3,7,9):
                    c=2
                elif b==2:
                    c=9
            elif b2==7:
                if b in (1,3,4,9):
                    c=2
                elif b==2:
                    c=1
            elif b2==3:
                if b in (2,4,7,8):
                    c=1
                elif b==1:
                    c=2
            elif b2==8:
                if b in (2,3,4,7):
                    c=1
                elif b==1:
                    c=7
            elif b2==2:
                if b in (1,4,8,9):
                    c=7
                elif b==7:
                    c=9
            elif b2==9:
                if b in (1,2,4,8):
                    c=7
                elif b==7:
                    c=8
        elif b1==7:
            if b2==2:
                if b==1:
                    c=4
                elif b==4:
                    c=1
                elif b==6:
                    c=9
                elif b==8:
                    c=9
                elif b==9:
                    c=8
            elif b2==6:
                if b==1:
                    c=4
                elif b==2:
                    c=1
                elif b==4:
                    c=1
                elif b==8:
                    c=9
                elif b==9:
                    c=8
            elif b2==9:
                if b in (1,3,4,6):
                    c=2
                elif b==2:
                    c=4
            elif b2==8:
                if b in (2,3,4,6):
                    c=1
                elif b==1:
                    c=4
            elif b2==1:
                if b in (2,3,8,9):
                    c=6
                elif b==6:
                    c=2
            elif b2==4:
                if b in (2,3,6,8):
                    c=9
                elif b==9:
                    c=8
            elif b2==3:
                if b in (1,4,6,9):
                    c=8
                elif b==8:
                    c=9
        elif b1==8:
            if b2==1:
                if b in (2,3,7,9):
                    c=6
                elif b==6:
                    c=3
            elif b2==2:
                if b in (1,3,7,9):
                    c=6
                elif b==6:
                    c=1
            elif b2==3:
                if b in (1,2,7,9):
                    c=6
                elif b==6:
                    c=9
            elif b2==4:
                if b in (1,2,6,9):
                    c=3
                elif b==3:
                    c=1
            elif b2==9:
                if b in (1,2,4,6):
                    c=3
                elif b==3:
                    c=6
            elif b2==6:
                if b in (2,3,4,7):
                    c=1
                elif b==1:
                    c=3
            elif b2==7:
                if b in (2,3,4,6):
                    c=1
                elif b==1:
                    c=4
        elif b1==9:
            if b2==2:
                if b==3:
                    c=6
                elif b==4:
                    c=3
                elif b==6:
                    c=3
                elif b==7:
                    c=4
                elif b==8:
                    c=7
            elif b2==4:
                if b==2:
                    c=3
                elif b==3:
                    c=6
                elif b==6:
                    c=3
                elif b==7:
                    c=8
                elif b==8:
                    c=7
            elif b2==7:
                if b in (1,3,4,6):
                    c=2
                elif b==2:
                    c=4
            elif b2==8:      
                if b in (1,2,4,6):
                    c=3
                elif b==3:
                    c=6
            elif b2==3:
                if b in (1,2,7,8):
                    c=4
                elif b==4:
                    c=8
            elif b2==6:
                if b in (1,2,4,8):
                    c=7
                elif b==7:
                    c=8
            elif b2==1:
                if b in (2,3,7,8):
                    c=6
                elif b==6:
                    c=3
        b3=b
    elif a2==4:
        if b1==1:
            if b2==6:
                if b3==2: 
                    if b in (4,8):
                        c=7
                    elif b==7:
                        c=4
                elif b3==3:
                    if b in (4,7):
                        c=8
                    elif b==8:
                        c=4
                elif b3==4:
                    if b in (2,3):
                        c=8
                    elif b in (2,8):
                        c=3
                elif b3==7:
                    if b==2:
                        c=3
                    elif b==3:
                        c=2
                    elif b==8:
                        c=2
                elif b3==8:
                    if b in (2,4):
                        c=4
                    elif b==3:
                        c=2
            elif b2==8:
                if b3==2:
                    if b in (4,6):
                        c=7
                    elif b in (4,7):
                        c=6
                elif b3==3:
                    if b==4:
                        c=7
                    elif b==7:
                        c=4
                    elif b==6:
                        c=4
                elif b3==4:
                    if b in (2,6):
                        c=3
                    elif b==3:
                        c=2
                elif b3==7:
                    if b in (2,3):
                        c=6
                    elif c==6:
                        c=3
                elif b3==6:
                    if b in (2,4):
                        c=7
                    elif b==7:
                        c=4
            elif b2==2:
                if b in (6,8):
                    c=9
                elif b==9:
                    c=8
            elif b2==3:
                if b in (7,9):
                    c=6
                elif b==6:
                    c=9
            elif b2==4:
                if b in (6,8):
                    c=9
                elif b==9:
                    c=6
            elif b2==7:
                if b in (3,9):
                    c=2
                elif b==2:
                    c=3
            elif b2==9:
                if b in (4,6):
                    c=7
                elif b==7:
                    c=4
        elif b1==2:
            if b2==7:
                if b in (3,8):
                    c=9
                elif b==9:
                    c=8
            elif b2==8:
                if b in (3,7):
                    c=1
                elif b==1:
                    c=3
            elif b2==9:
                if b in (1,8):
                    c=3
                elif b==3:
                    c=1
            elif b2==1:
                if b in (8,9):
                    c=6
                elif b==6:
                    c=9
            elif b2==6:
                if b in (4,8):
                    c=1
                elif b==1:
                    c=4
            elif b2==3:
                if b in (7,8):
                    c=4
                elif b==4:
                    c=7
            elif b2==4:
                if b in (6,8):
                    c=7
                elif b==7:
                    c=8
        elif b1==3:
            if b2==4:
                if b3==1:
                    if b in (6,9):
                        c=8
                    elif b==8:
                        c=9
                elif b3==2:
                    if b in (6,8):
                        c=9
                    elif b==9:
                        c=6
                elif b3==6:
                    if b in (1,2):
                        c=8
                    elif b in (2,8):
                        c=1
                elif b3==8:
                    if b in (2,6):
                        c=1
                    elif b==1:
                        c=2
                elif b3==9:
                    if b in (1,8):
                        c=2
                    elif b==2:
                        c=1
            elif b2==8:
                if b3==1:
                    if b in (4,6):
                        c=9
                    elif b==9:
                        c=6
                elif b3==2:
                    if b in (4,6):
                        c=9
                    elif b in (6,9):
                        c=4
                elif b3==4:
                    if b in (2,6):
                        c=9
                    elif b==9:
                        c=6
                elif b3==6:
                    if b in (2,4):
                        c=1
                    elif b==1:
                        c=2
                elif b3==9:
                    if b in (1,2):
                        c=4
                    elif b==4:
                        c=1
            elif b2==1:
                if b in (7,9):
                    c=6
                elif b==6:
                    c=9
            elif b2==2:
                if b in (7,8):
                    c=4
                elif b==4:
                    c=7
            elif b2==6:
                if b in (4,7):
                    c=8
                elif b==8:
                    c=7
            elif b2==7:
                if b in (4,6):
                    c=9
                elif b==9:
                    c=6
            elif b2==9:
                if b in (1,7):
                    c=2
                elif b==2:
                    c=1
        elif b1==4:
            if b2==3:
                if b in (6,7):
                    c=1
                elif b==1:
                    c=7
            elif b2==9:
                if b in (1,6):
                    c=3
                elif b==3:
                    c=6
            elif b2==6:
                if b in (1,9):
                    c=7
                elif b in (7,9):
                    c=1
            elif b2==1:
                if b in (6,9):
                    c=8
                elif b==8:
                    c=9
            elif b2==8:
                if b in (2,6):
                    c=9
                elif b==9:
                    c=6
            elif b2==2:
                if b in (6,8):
                    c=7
                elif b==7:
                    c=8
            elif b2==7:
                if b in (3,6):
                    c=2
                elif b==2:
                    c=3
        elif b1==5:
            if b2==2:
                if b3==3:
                    if b in (6,9):
                        c=4
                    elif b==4:
                        c=6
                elif b3==4:
                    if b in (3,9):
                        c=7
                    elif b in (7,9):
                        c=3
                elif b3==6:
                    if b in (3,9):
                        c=7
                    elif b==7:
                        c=3
                elif b3==7:
                    if b in (4,9):
                        c=6
                    elif b==6:
                        c=4
                elif b3==9:
                    if b in (3,6):
                        c=4
                    elif b==4:
                        c=6
            elif b2==3:
                if b in (2,9):
                    c=8
                elif b==8:
                    c=2
            elif b2==4:
                if b3==2:
                    if b in (3,9):
                        c=7
                    if b==7:
                        c=3
                elif b3==3:
                    if b in (2,9):
                        c=8
                    elif b==8:
                        c=2
                elif b3==7:
                    if b in (8,9):
                        c=2
                    elif b==2:
                        c=8
                elif b3==8:
                    if b in (7,9):
                        c=3
                    elif b==3:
                        c=7
                elif b3==9:
                    if b in (7,8):
                        c=2
                    elif b==2:
                        c=8
            elif b2==6:
                if b in (8,9):
                    c=2
                elif b==2:
                    c=8
            elif b2==7:
                if b in (4,9):
                    c=6
                elif b==6:
                    c=4
            elif b2==8:
                if b in (6,9):
                    c=4
                elif b==4:
                    c=6
            elif b2==9:
                if b in (2,3):
                    c=8
                elif b==8:
                    c=2
        elif b1==6:
            if b2==1:
                if b in (4,9):
                    c=7
                elif b==7:
                    c=4
            elif b2==4:
                if b in (1,3):
                    c=7
                elif b==(7,3):
                    c=1
            elif b2==7:
                if b in (3,4):
                    c=9
                elif b in 9:
                    c=4
            elif b2==3:
                if b in (4,7):
                    c=8
                elif b==8:
                    c=7
            elif b2==8:
                if b in (2,4):
                    c=3
                elif b==3:
                    c=2
            elif b2==2:
                if b in (4,8):
                    c=1
                elif b==1:
                    c=4
            elif b2==9:
                if b in (1,4):
                    c=2
                elif b==2:
                    c=1
        elif b1==7:
            if b2==2:
                if b3==1:
                    if b in (8,9):
                        c=6
                    elif b==6:
                        c=9
                elif b3==4:
                    if b in (6,8):
                        c=9
                    elif b==9:
                        c=8
                elif b3==6:
                    if b in (4,8):
                        c=1
                    elif b==1:
                        c=4
                elif b3==8:
                    if b in (1,4):
                        c=6
                    elif b==(4,6):
                        c=1
                elif b3==9:
                    if b in (1,6):
                        c=4
                    elif b==4:
                        c=1
            elif b2==6:
                if b3==1:
                    if b in (2,8):
                        c=9
                    elif b==9:
                        c=8
                elif b3==2:
                    if b in (4,8):
                        c=9
                    elif b==9:
                        c=8
                elif b3==4:
                    if b in (2,8):
                        c=9
                    elif b in (8,9):
                        c=2
                elif b3==8:
                    if b in (2,4):
                        c=1
                    elif b==1:
                        c=4
                elif b3==9:
                    if b in (1,4):
                        c=2
                    elif b==2:
                        c=1
            elif b2==9:
                if b in (1,3):
                    c=6
                elif b==6:
                    c=3
            elif b2==8:
                if b in (2,3):
                    c=6
                elif b==6:
                    c=3
            elif b2==1:
                if b in (3,9):
                    c=8
                elif b==8:
                    c=9
            elif b2==4:
                if b in (3,6):
                    c=2
                elif b==2:
                    c=3
            elif b2==3:
                if b in (4,6):
                    c=1
                elif b==1:
                    c=4
        elif b1==8:
            if b2==1:
                if b in (2,9):
                    c=7
                elif b==7:
                    c=9
            elif b2==2:
                if b in (3,9):
                    c=7
                elif b in (3,7):
                    c=9
            elif b2==3:
                if b in (2,7):
                    c=1
                elif b==1:
                    c=2
            elif b2==4:
                if b in (2,6):
                    c=9
                elif b==9:
                    c=6
            elif b2==9:
                if b in (1,2):
                    c=4
                elif b==4:
                    c=1
            elif b2==6:
                if b in (2,4):
                    c=7
                elif b==7:
                    c=4
            elif b2==7:
                if b in (2,3):
                    c=6
                elif b==6:
                    c=3
        elif b1==9:
            if b2==2:
                if b3==3:
                    if b in (7,8):
                        c=4
                    elif b==4:
                        c=7
                elif b3==4:
                    if b in (6,8):
                        c=7
                    elif b==7:
                        c=8
                elif b3==6:
                    if b in (4,8):
                        c=7
                    elif b==7:
                        c=8
                elif b3==7:
                    if b in (4,6):
                        c=3
                    elif b==3:
                        c=6
                elif b3==8:
                    if b in (3,6):
                        c=4
                    elif b in (4,6):
                        c=3
            elif b2==4:
                if b3==2:
                    if b in (6,8):
                        c=7
                    elif b==7:
                        c=8
                elif b3==3:
                    if b in (2,8):
                        c=7
                    elif b in (2,7):
                        c=8
                elif b3==6:
                    if b in (2,8):
                        c=7
                    elif b==7:
                        c=2
                elif b3==7:
                    if b in (3,6):
                        c=2
                    elif b==2:
                        c=3
                elif b3==8:
                    if b in (2,6):
                        c=3
                    elif b==3:
                        c=6
            elif b2==7:
                if b in (1,3):
                    c=6
                elif b==6:
                    c=3
            elif b2==8:
                if b in (1,2):
                    c=4
                elif b==4:
                    c=1
            elif b2==3:
                if b in (1,7):
                    c=2
                elif b==2:
                    c=1
            elif b2==6:
                if b in (1,4):
                    c=2
                elif b==2:
                    c=1
            elif b2==1:
                if b in (2,8):
                    c=7
                elif b==7:
                    c=8
    a[c]='O'
    print(a[1], '|', a[2], '|', a[3])
    print('--+---+--')
    print(a[4], '|', a[5], '|', a[6])
    print('--+---+--')
    print(a[7], '|', a[8], '|', a[9])
    print('\n',_format_)