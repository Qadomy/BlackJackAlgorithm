import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9
               ,'10':10, 'J':10, 'Q':10, 'K':10, 'A':11}


class blackJack():


    """"Here for create the 52 of different cards"""
    cards = []
    for suit in suits:
        for rank in ranks:
            cards.append((rank, suit))

    new_dictionary = {}

    totall = 0
    def calculateValueForPlayer(self):
        value = []
        for i in self.new_dictionary.keys():
            for k in card_values.keys():
                if i == k:
                    value.append(card_values[k])
        self.totall = sum(value)
        #print(value)
                    #print(self.totall)
        print("And Your Value {}".format(self.totall))




    player_cards = []
    """Display the cards of player"""
    def player_turn(self):
        while len(self.player_cards) != 2:
            self.player_cards.append(random.choice(self.cards)) # random.choice: for a lists

            if len(self.player_cards) == 2:
                print("You have {}".format(self.player_cards))

                self.new_dictionary.update(self.player_cards)
                #print(self.new_dictionary)
                self.calculateValueForPlayer()




    dealer_cards = []
    """Display the cards of Dealer"""
    def dealer_turn(self):
        while len(self.dealer_cards) != 2:
            self.dealer_cards.append(random.choice(self.cards))

            if len(self.dealer_cards) == 2:
                print("Dealer has X , {}".format(self.dealer_cards[1]))
        #return dealer_cards

    new_dictionary2 = {}
    def stand(self):
        while len(self.dealer_cards) != 2:
            self.dealer_cards.append(random.choice(self.cards)) # random.choice: for a lists

            if len(self.dealer_cards) == 2:
                print("Dealer have {}".format(self.dealer_cards))

                self.new_dictionary2.update(self.dealer_cards)
                #print(self.new_dictionary)
                #self.calculateValueForDealer()

            self.calculateScoreDealer()



        while self.total < 17:
            #self.dealer_turn()
            self.dealer_cards.append(random.choice(self.cards))
            print(self.dealer_cards)
            self.new_dictionary2.update(self.dealer_cards)
            self.calculateScoreDealer()



    total = 0
    def calculateScoreDealer(self):
        value = []
        for i, j in self.new_dictionary2.items():
            for k, l in card_values.items():
                if i == k:
                    value.append(l)
                    self.total = sum(value)
        print(value)
        print("Dealer Value {}".format(self.total))



    """Here for calculate the Score when A come"""
    def calculateScore(self):
        value = []
        for i, j in self.new_dictionary.items():
            for k, l in card_values.items():
                if i == k:
                    ass = l
                    value.append(ass)
                    total = sum(value)

    def hit(self):
        #self.player_turn() # yup I found It hahahaha
        self.player_cards.append(random.choice(self.cards))
        print(self.player_cards)
        self.new_dictionary.update(self.player_cards)
        self.calculateValueForPlayer()

    inputHS = ''
    def main(self):
        player_name = ''
        #player_name = str(input("Enter Your name: "))
        #print("Welcome {}, To BLACKJACK!".format(player_name))

        players = [player_name, 'Dealer']

        for player in players:
            #print("'{}' your turn starts now!".format(player))

            if player == player_name:
                print("You have {} cards".format(self.player_turn()))
                while True:
                    self.inputHS = input("Did you want hit or stand ? ")

                    if self.inputHS.lower() == 'hit':
                        self.hit()
                        self.calculateScore()



                    elif self.inputHS.lower() == 'stand':
                        if self.totall > 21:
                            print("BUSTED Dealer WON !!!")
                            break
                        else:
                            self.stand()
                        break



            elif player == 'Dealer':
                print("Dealer have {} cards".format(self.dealer_turn()))

                self.showWinner()

    def showWinner(self):
        if self.totall > self.total and self.totall < 21:
            print("You Won!!")
        elif self.totall == 21 and self.total != 21:
            print("BLACK JACK YOU WON!!")
        elif self.total > self.totall and self.total <= 21:
            print("BUSTED Dealer WON !!!")
        elif self.total == 21 and self.totall < 21:
            print("BUSTED!!")
        elif self.totall <= 21 and self.total <= 21 and self.total == self.totall:
            print("Push")
        elif self.totall > 21 and self.total <= 21:
            print("BUSTED Dealer WON !!!")
        else:
            print("*********HOBLA*********")



test = blackJack()
test.main()
