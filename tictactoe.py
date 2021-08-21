table={"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}

player=1
moves=1
check=0

print("<===========positions===========>")
print('1'," |",'2'," |",'3')
print("---+----+---")
print('4'," |",'5'," |",'6')
print("---+----+---")
print('7'," |",'8'," |",'9')
print("<================================>")

def rules():
    #horizonatal rules
    if table['1']=='X' and table['2']=='X' and table['3']=='X':
        print("Player 1 Won!")
        return 1
    if table['4']=='X' and table['5']=='X' and table['6']=='X':
        print("Player 1 Won!")
        return 1
    if table['7']=='X' and table['8']=='X' and table['9']=='X':
        print("Player 1 Won!")
        return 1
    if table['1']=='O' and table['2']=='O' and table['3']=='O':
        print("Player 2 Won!")
        return 1
    if table['4']=='O' and table['5']=='O' and table['6']=='O':
        print("Player 2 Won!")
        return 1
    if table['7']=='O' and table['8']=='O' and table['9']=='O':
        print("Player 2 Won!")
        return 1
    
    #vertical rules
    if table['1']=='X' and table['4']=='X' and table['7']=='X':
        print("Player 1 Won!")
        return 1
    if table['2']=='X' and table['5']=='X' and table['8']=='X':
        print("Player 1 Won!")
        return 1
    if table['3']=='X' and table['6']=='X' and table['9']=='X':
        print("Player 1 Won!")
        return 1
    if table['1']=='O' and table['4']=='O' and table['7']=='O':
        print("Player 2 Won!")
        return 1
    if table['2']=='O' and table['5']=='O' and table['8']=='O':
        print("Player 2 Won!")
        return 1
    if table['3']=='O' and table['6']=='O' and table['9']=='O':
        print("Player 2 Won!")
        return 1
    
    #diagonal rules
    if table['1']=='X' and table['5']=='X' and table['9']=='X':
        print("player 1 Won!")
        return 1
    if table['3']=='X' and table['5']=='X' and table['7']=='X':
        print("player 1 Won!")
        return 1
    if table['1']=='O' and table['5']=='O' and table['9']=='O':
        print("player 2 Won!")
        return 1
    if table['3']=='O' and table['5']=='O' and table['7']=='O':
        print("player 2 Won!")
        return 1

    return 0

def tictactoe():
    player=1
    moves=1
    check=0
    print("<=============start==============>")

    while True:
        print(table['1']," |",table['2']," |",table['3'])
        print("---+----+---")
        print(table['4']," |",table['5']," |",table['6'])
        print("---+----+---")
        print(table['7']," |",table['8']," |",table['9'])
        print("<================================>")

        check=rules()

        if(moves>=9) or check==1:
            break

        while True:
            if player==1:
                player1_input=input("player 1 chance : ")
                if player1_input in table and table[player1_input]==' ':
                    table[player1_input]='X'
                    player=2
                    break
                else:
                    print("Invalid input,try again")
                    continue
            else:
                player2_input=input("player 2 chance: ")
                if player2_input in table and table[player2_input]==' ':
                    table[player2_input]='O'
                    player=1
                    break
                else:
                    print("Invalid input,try again")
                    player=2
                

            moves+=1
            print("<================================>")

    playagain=input("wanna play again? (yes or no): ")
    if playagain=='yes':
        table['1']=" "
        table['2']=" "
        table['3']=" "
        table['4']=" "
        table['5']=" "
        table['6']=" "
        table['7']=" "
        table['8']=" "
        table['9']=" "
        tictactoe()
    else:
        print("quiting")
        exit()

tictactoe()