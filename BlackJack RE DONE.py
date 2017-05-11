#total points at end of game
import random

#Deck
deck = ['Ace of Hearts,', '2 of Hearts,', '3 of Hearts,', '4 of Hearts,', '5 of Hearts,', '6 of Hearts,', '7 of Hearts,', '8 of Hearts,', '9 of Hearts,', '10 of Hearts,', 'Jack of Hearts,', 'Queen of Hearts,','King of Hearts,', 'Ace of Diamonds,','2 of Diamonds,', '3 of Diamonds,','4 of Diamonds,', '5 of Diamonds,', '6 of Diamonds,', '7 of Diamonds,', '8 of Diamonds,', '9 of Diamonds,', '10 of Diamonds,', 'Jack of Diamonds,', 'Queen of Diamonds,', 'King of Diamonds,', 'Ace of Spades,', '2 of Spades,', '3 of Spades,', '4 of Spades,', '5 of Spades,', '6 of Spades,', '7 of Spades,', '8 of Spades,', '9 of Spades,', '10 of Spades,', 'Jack of Spades,', 'Queen of Spades,', 'King of Spades,', 'Ace of Clubs,', '2 of Clubs,', '3 of Clubs,', '4 of Clubs,', '5 of Clubs,', '6 of Clubs,', '7 of Clubs,', '8 of Clubs,', '9 of Clubs,', '10 of Clubs,', 'Jack of Clubs,', 'Queen of Clubs,', 'King of Clubs,',   ]
value = {'Ace of Hearts,':11, '2 of Hearts,':2, '3 of Hearts,':3, '4 of Hearts,':4, '5 of Hearts,':5, '6 of Hearts,':6, '7 of Hearts,':7, '8 of Hearts,':8, '9 of Hearts,':9, '10 of Hearts,':10, 'Jack of Hearts,':10, 'Queen of Hearts,':10,'King of Hearts,':10, 'Ace of Diamonds,':11,'2 of Diamonds,':2, '3 of Diamonds,':3,'4 of Diamonds,':4, '5 of Diamonds,':5, '6 of Diamonds,':6, '7 of Diamonds,':7, '8 of Diamonds,':8, '9 of Diamonds,':9, '10 of Diamonds,':10, 'Jack of Diamonds,':10, 'Queen of Diamonds,':10, 'King of Diamonds,':10, 'Ace of Spades,':11, '2 of Spades,':2, '3 of Spades,':3, '4 of Spades,':4, '5 of Spades,':5, '6 of Spades,':6, '7 of Spades,':7, '8 of Spades,':8, '9 of Spades,':9, '10 of Spades,':10, 'Jack of Spades,':10, 'Queen of Spades,':10, 'King of Spades,':10, 'Ace of Clubs,':11, '2 of Clubs,':2, '3 of Clubs,':3, '4 of Clubs,':4, '5 of Clubs,':5, '6 of Clubs,':6, '7 of Clubs,':7, '8 of Clubs,':8, '9 of Clubs,':9, '10 of Clubs,':10, 'Jack of Clubs,':10, 'Queen of Clubs,':10, 'King of Clubs,':10}
random.shuffle(deck)

#Game
def BLACKJACK():
    print ("\n\n-------------------------------- New Game --------------------------------")
    print ("")
#Hands
    player = [deck.pop() for _ in range(2)]
    cpu = [deck.pop() for _ in range(2)]
    
#Printing player hand
    print ("\nThe two cards you're dealt are:")
    print(*player)
    
#printing cpu hand
    print ("\nThe dealers showing card is a:")
    print (cpu[0])

#Hand Values
    player_hand = sum(map(value.get, player ))
    cpu_hand = sum(map(value.get, cpu ))
    
#BlackJack hand


#Tie 2 card 21
    for _ in range(1):
        if len(player) < 3 and len(cpu) <3:
            if player_hand == 21 and cpu_hand == 21:
                print ("Both you and the deal got a 2 card 21, also called a BlackJack. Its a 'Push', also called a tie.")
                print ("\n\nYour cards:", *player)
                print ("Your total points:", player_hand)
                print ('\nDealers cards:', *cpu)
                print ("Dealers total points:", cpu_hand)
                ######
                play_again = input("\n\nWould you like to play again? (yes/no) ")
                if play_again.lower() == ("yes"):
                    BLACKJACK()
                if play_again.lower() == ("no"):
                    print ("Thank you for playing. Goodbye.")
                    quit()
                else:
                    print ("Please enter 'yes' or 'no'. other answers will not be accepted.")

#player 2 card 21
        if len(player) < 3:
            if (player_hand) == 21:
                print ("\nYou got a 2 card 21, also called a BlackJack. You automaticaly win!")
                print ("\n\nYour cards:", *player)
                print ("Your total points:", player_hand)
                print ("\nDealers cards:", *cpu)
                print ("Dealers total points:", cpu_hand)
                #####
                play_again = input("\n\nWould you like to play again? yes/no")
                if play_again.lower() == ("yes"):
                    BLACKJACK()
                if play_again.lower() == ("no"):
                    print ("Thank you for playing. Goodbye.")
                    quit()
                else:
                    print ("Please enter 'yes' or 'no'. other answers will not be accepted.")

#CPU 2 card 21
        if len(cpu) < 3:
            if (cpu_hand) == 21:
                print ("\nThe Dealer got a 2 card 21, also called a BlackJack. The deal automaticaly wins.")
                print ("\n\nYour cards:", *player)
                print ("Your total points:", player_hand)
                print ("\nDealers cards:", *cpu)
                print ("Dealers total points:", cpu_hand)
                #####
                play_again = input("\n\nWould you like to play again? yes/no")
                if play_again.lower() == ("yes"):
                    BLACKJACK()
                if play_again.lower() == ("no"):
                    print ("Thank you for playing. Goodbye.")
                    quit()
                else:
                    print ("Please enter 'yes' or 'no'. other answers will not be accepted.")

#Player 'Hitting' and 'Standing'             
    for _ in range(100):
        player_hit = input ("\n\nEnter 'hit' if you would like another card. or enter 'stand' if you like your hand and dont want another card.")

        if player_hit == ("hit"):
            player.append(deck.pop())
            player_hand = sum(map(value.get, player ))
            print ("\nThe following cards are in your hand:")
            print (*player)
            print ("")
            
#player Aces
            #Hearts
            if 'Ace of Hearts,' in player:
                if player_hand < 11:
                    value['Ace of Hearts,'] = 11
                    player_hand = sum(map(value.get, player ))
    
            if 'Ace of Hearts,' in player:
                if player_hand > 21:
                    value['Ace of Hearts,'] = 1
                    player_hand = sum(map(value.get, player ))
                    
            #Diamonds
            if 'Ace of Diamonds,' in player:
                if player_hand < 11:
                    value['Ace of Diamonds,'] = 11
                    player_hand = sum(map(value.get, player ))
                    
            if 'Ace of Diamonds,' in player:
                if player_hand > 21:
                    value['Ace of Diamonds,'] = 1
                    player_hand = sum(map(value.get, player ))
                    
            #Clubs
            if 'Ace of Clubs,' in player:
                if player_hand < 11:
                    value['Ace of Clubs,'] = 11
                    player_hand = sum(map(value.get, player ))
                    
            if 'Ace of Clubs,' in player:
                if player_hand > 21:
                    value['Ace of Clubs,'] = 1
                    player_hand = sum(map(value.get, player ))
                    
            #Spades
            if 'Ace of Spades,' in player:
                if player_hand < 11:
                    value['Ace of Spades,'] = 11
                    player_hand = sum(map(value.get, player ))
                    
            if 'Ace of Spades,' in player:
                if player_hand > 21:
                    value['Ace of Spades,'] = 1
                    player_hand = sum(map(value.get, player ))

#Player Busting:
            if player_hand > 21:
                print ("\nYou Busted!")
                print ("\n\nYour cards:", *player)
                print ("Your total points:", player_hand)
                print ("\nDealers cards:", *cpu)
                print ("Dealers total points:", cpu_hand)
                #####
                play_again = input("\n\nWould you like to play again? yes/no")
                if play_again.lower() == ("yes"):
                    BLACKJACK()
                if play_again.lower() == ("no"):
                    print ("Thank you for playing. Goodbye.")
                    quit()
                else:
                    print ("Please enter 'yes' or 'no'. other answers will not be accepted.")
                    return

#Player hand size:
            if len(player) > 4:
                print ("You have 5 cards in your hand. You automatically win.")
                print ("\n\nYour cards:", *player)
                print ("Your total points:", player_hand)
                print ("\nDealers cards:", *cpu)
                print ("Dealers total points:", cpu_hand)
                #####
                play_again = input("\n\nWould you like to play again? yes/no")
                if play_again.lower() == ("yes"):
                    BLACKJACK()
                if play_again.lower() == ("no"):
                    print ("Thank you for playing. Goodbye.")
                    quit()
                else:
                    print ("Please enter 'yes' or 'no'. other answers will not be accepted.")

        if player_hit == ("stand"):
            break
        else:
            print ("\nPlaese enter 'hit' or 'stand'. Other answers will not be accepted.")
        
#cpu 'Hitting' and 'Standing'
    for _ in range(20):        
        if cpu_hand < 17:
            cpu.append(deck.pop())
            cpu_hand = sum(map(value.get, cpu ))
            print ("\nThe dealer took a 'hit'.")

#cpu Aces
            #Hearts
            if 'Ace of Hearts,' in cpu:
                if cpu_hand < 11:
                    value['Ace of Hearts,'] = 11
                    cpu_hand = sum(map(value.get, player ))
    
            if 'Ace of Hearts,' in cpu:
                if cpu_hand > 21:
                    value['Ace of Hearts,'] = 1
                    cpu_hand = sum(map(value.get, player ))
                    
            #Diamonds
            if 'Ace of Diamonds,' in cpu:
                if cpu_hand < 11:
                    value['Ace of Diamonds,'] = 11
                    cpu_hand = sum(map(value.get, player ))
                    
            if 'Ace of Diamonds,' in cpu:
                if cpu_hand > 21:
                    value['Ace of Diamonds,'] = 1
                    cpu_hand = sum(map(value.get, player ))
                    
            #Clubs
            if 'Ace of Clubs,' in cpu:
                if cpu_hand < 11:
                    value['Ace of Clubs,'] = 11
                    cpu_hand = sum(map(value.get, player ))
                    
            if 'Ace of Clubs,' in player:
                if cpu_hand > 21:
                    value['Ace of Clubs,'] = 1
                    cpu_hand = sum(map(value.get, player ))
                    
            #Spades
            if 'Ace of Spades,' in cpu:
                if cpu_hand < 11:
                    value['Ace of Spades,'] = 11
                    cpu_hand = sum(map(value.get, player ))
                    
            if 'Ace of Spades,' in cpu:
                if cpu_hand > 21:
                    value['Ace of Spades,'] = 1
                    cpu_hand = sum(map(value.get, player ))

#cpu Busting
            if cpu_hand > 21:
                print ("\nThe dealer Busted!")
                print ("\n\nYour cards:", *player)
                print ("Your total points:", player_hand)
                print ('\nDealers cards:', *cpu)
                print ("Dealers total points:", cpu_hand)

                #####
                play_again = input("\n\nWould you like to play again? yes/no")
                if play_again.lower() == ("yes"):
                    BLACKJACK()
                if play_again.lower() == ("no"):
                    print ("Thank you for playing. Goodbye.")
                    quit()
                else:
                    print ("Please enter 'yes' or 'no'. other answers will not be accepted.")

#CPU hand size
            if len(cpu) > 4:
                print ("\nThe dealer has 5 cards. The dealer automaticaly wins.")
                print ('\n\nYour cards:', *player)
                print ("Your total points:", player_hand)
                print ('\nDealers cards:', *cpu)
                print ("Dealers total points:", cpu_hand)
                #####
                play_again = input("\n\nWould you like to play again? yes/no")
                if play_again.lower() == ("yes"):
                    BLACKJACK()
                if play_again.lower() == ("no"):
                    print ("Thank you for playing. Goodbye.")
                    quit()
                else:
                    print ("Please enter 'yes' or 'no'. other answers will not be accepted.")

        else:
            print ("\nThe dealer stood.")
            print ("\nThe dealer is showing th cards:", *cpu)
            break
        
#Comparing total points and winning with high score

    #Player winning by high score
    for _ in range(1):
        if player_hand > cpu_hand:
            print ("\n\nYour score was closer to 21 than the dealers. You Win!")
            print ('\n\nYour cards:', *player)
            print ("Your total points:", player_hand)
            print ('\nDealers cards:', *cpu)
            print ("Dealers total points:", cpu_hand)
            #####
            play_again = input("\n\nWould you like to play again? yes/no")
            if play_again.lower() == ("yes"):
                BLACKJACK()
            if play_again.lower() == ("no"):
                print ("Thank you for playing. Goodbye.")
                quit()
            else:
                print ("Please enter 'yes' or 'no'. other answers will not be accepted.")

#CPU winning by high score
        if cpu_hand > player_hand:
            print ("\n\nThe dealers score was closer to 21 than yours. The Dealer Wins!")
            print ('\n\nYour cards:', *player)
            print ("Your total points:", player_hand)
            print ('\nDealers cards:', *cpu)
            print ("Dealers total points:", cpu_hand)
            #####
            play_again = input("\n\nWould you like to play again? yes/no")
            if play_again.lower() == ("yes"):
                BLACKJACK()
            if play_again.lower() == ("no"):
                print ("Thank you for playing. Goodbye.")
                quit()
            else:
                print ("Please enter 'yes' or 'no'. other answers will not be accepted.")
                
#Winning by push
        if player_hand == cpu_hand:
            print ("\nYou and the dealers hands have the same total score. Its a tie, also called a 'push'.")
            print ('\n\nYour cards:', *player)
            print ("Your total points:", player_hand)
            print ('\nDealers cards:', *cpu)
            print ("Dealers total points:", cpu_hand)
            #####
            play_again = input("\n\nWould you like to play again? yes/no")
            if play_again.lower() == ("yes"):
                BLACKJACK()
            if play_again.lower() == ("no"):
                print ("Thank you for playing. Goodbye.")
                quit()
            else:
                print ("Please enter 'yes' or 'no'. other answers will not be accepted.")
        break
    
BLACKJACK()

