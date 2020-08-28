class Deck:
    def __init__(self):
        self.deck = []

    def __str__(self):
        return str(self.deck)

    def __len__(self):
        return len(self.deck)

    def __getitem__(self,item):
        return self.deck[item]

    def build(self):
        suits = ["♣", "♦", "♥", "♠"]
        card_face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for i in suits:
            for j in card_face:
                self.deck.append(i + j)


class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return str(self.hand)

    def draw(self, cards):
        import random
        n = 0
        while n < cards:
            index = random.randrange(0, len(deck))
            self.hand.append(deck[index])
            deck.deck.remove(self.hand[len(self.hand) - 1])
            n += 1
        print(self.hand)

    def value(self):
        card_face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        hand_value = 0
        for n in range(len(self.hand)):
            for m in range(len(card_face)):
                if self.hand[n][1:] == card_face[m]:
                    hand_value += card_value[m]
        print("The value of your hand is {}".format(hand_value))

deck = Deck()
deck.build()
terry = Hand()
terry.draw(2)
terry.value()
