import random
dealer_cards = []
player_cards = []
card_options = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

while len(dealer_cards) != 2:
   dealer_cards.append(card_options[random.randint(0,12)])
   if len(dealer_cards) == 2:
       print("Dealer has X &", dealer_cards[1])

while len(player_cards) != 2:
   player_cards.append(card_options[random.randint(0,12)])
   if len(player_cards) == 2:
       print("You have " + str(player_cards))

if sum(dealer_cards) == 21:
   print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
   print("Dealer has busted")

while sum(player_cards) < 21:
   action_taken = str(input("Do you want to stay or hit? "))
   if action_taken == "hit" or action_taken =="Hit" or action_taken =="h":
       player_cards.append(card_options[random.randint(0,12)])
       print("You now have " + str(sum(player_cards)) + " from these cards", player_cards)
   else:
       print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
       print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
       if sum(dealer_cards) > sum(player_cards):
           print("Dealer wins!")
       else:
           print("You win!")
           break
if sum(player_cards) > 21:
   print("You busted. Dealer wins.")
elif sum(player_cards) == 21:
   print("You have BLACKJACK! You Win! 21!")
