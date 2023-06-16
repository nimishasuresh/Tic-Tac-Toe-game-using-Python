#import random

play_card = [' '] * 10
player_one = 'X'
player_two = 'O'
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("******WELCOME TO TIC TAC TOE GAME******")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
print("Instructions.........")
print("1.Players take turns putting their marks in empty squares.")
print("2.The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
print("3.When all 9 squares are full, the game is over.")
print("4.If no player has 3 marks in a row, the game ends in a tie.")
print("\n")
try:
    print("Are you ready for playing the game!!!!")
    confirm =input('------Yes Or No----------')

    def display(play_card):
    
        print("----------")
        print(f'|{play_card[1]} | {play_card[2]} |{play_card[3]} |')
        print("----------")
        print(f'|{play_card[4]} | {play_card[5]} |{play_card[6]} |')
        print("----------")
        print(f'|{play_card[7]} | {play_card[8]} |{play_card[9]} |')
        print('-' * 10)


    def check_win():
        if play_card[1] == play_card[2] == play_card[3] and play_card[1]!= ' ':
            return True
        elif play_card[4] == play_card[5] == play_card[6] and play_card[4]!=' ':
            return True
        elif play_card[7] == play_card[8] == play_card[9] and play_card[7]!=' ':
            return True
        elif play_card[1] == play_card[4] == play_card[7] and play_card[1]!=' ':
            return True
        elif play_card[2] == play_card[5] == play_card[8] and play_card[2]!=' ':
            return True
        elif play_card[3] == play_card[6] == play_card[9] and play_card[3]!=' ':
            return True
        elif play_card[1] == play_card[5] == play_card[9] and play_card[1]!=' ':
            return True
        elif play_card[3] == play_card[5] == play_card[7] and play_card[3]!=' ':
            return True
        else:
            return False


    def insert(letter, pos):
        if play_card[pos] == ' ':
            play_card[pos] = letter
            display(play_card)
            if check_win():
                if letter == 'X':
                    print("----------------------------------------")
                    print(f'.......{play1_name} wins the game......')
                    print("----------------------------------------")
                    display(play_card)
                    exit()
                else:
                    print("----------------------------------------")
                    print(f'.......{play2_name} wins the game......')
                    print("----------------------------------------") 
                    display(play_card)
                    exit()
            if play_card.count(' ') ==1:
                print(".......Its Tie......")
                exit()
        else:
            if letter == 'O':
                pos = int(input("Not Free! Please re-enter a position"))
            else:
            #pos = random.randint(1, 9)
                pos = int(input("Not Free! Please re-enter a position player2"))
            insert(letter, pos)
    if confirm == 'Yes':
        play1_name = input("Enter the player one name::::")
        play2_name = input("Enter the player Two name::::")
        
    
    
        def player1_move(letter):
        
            pos = int(input(f'{play1_name}!!please enter your number from 1 to 9...'))
            insert(letter, pos)
        
    else:
        print("Thank You!!!!")
        exit()

    def player2_move(letter):
        pos = int(input(f'{play2_name}!!please enter your number from 1 to 9...'))
        insert(letter, pos)


# main loop
    while not check_win():
        display(play_card)
        player1_move(player_one)
        player2_move(player_two)

except TypeError:
    print("invalid choice!!!")

except ValueError:
    print("Something Wrong!!!")
finally:
    print("Nothing Went Wrong!!!!")
    