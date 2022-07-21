import itertools
import random
import re


class teenpatti:

    def __init__(self) -> None:
        self.deck = [
                    'A', 'A', 'A', 'A',
                     '2', '2', '2', '2',
                     '3', '3', '3', '3',
                     '4', '4', '4', '4',
                     '5', '5', '5', '5',
                     '6', '6', '6', '6',
                     '7', '7', '7', '7',
                     '8', '8', '8', '8',
                     '9', '9', '9', '9',
                     '10', '10', '10', '10',
                     'J', 'J', 'J', 'J',
                     'Q', 'Q', 'Q', 'Q',
                     'K', 'K', 'K', 'K'
                     ]
        self.players_list = {}
        self.card = []
        for i in itertools.combinations(self.deck, 3):
            self.card.append(i)

    def distribute(self):
        for key,value in self.players_list.items():
            self.players_list[key] = random.choice(self.card)

        for key,value in self.players_list.items():
            print('\n')
            print(f'{key}:')
            for i in value:
                print(i, end='\t')

    def players(self):
        while True:
            y = input('Name of player:')
            x = re.search(r'\w+', y)
            if y == '':
                break
            elif x:
                self.players_list[y] = ''
            else:
                print('Invalid Name Input. \nPlease Provide Characters, Numbers & Underscore only.')

    def win_lose(self):
        for key1,value1 in self.players_list.items():
            for key2,value2 in self.players_list.items():
                pass

    def play(self):
        print(self.card)
        self.players()
        self.distribute()
        print(self.card)


if __name__ == '__main__':
    game = teenpatti()
    game.play()


# while True:
#     card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#     susan = random.choices(card, k=3)
#     anmol = random.choices(card, k=3)

#     print('Anmol:')
#     for i in anmol:
#         print(i,end='\t')

#     print('\nSusan:')
#     for i in susan:
#         print(i,end='\t')


#     x = input('\nPress e/E to exit.')
#     if x=='e' or x=='E':
#         exit()
