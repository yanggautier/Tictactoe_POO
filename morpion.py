'''
Le Morpion, également appelé Tic-Tac-Toe se joue sur une grille carrée de 3x3 cases. Deux joueurs, vous et l'ordinateur s'affrontent. Ils doivent remplir chacun à leur tour une case de la grille avec le symbole qui leur est attribué : O ou X.
Le gagnant est celui qui arrive à aligner trois symboles identiques, horizontalement, verticalement ou en diagonale.
'''

import random

class Morpion:
    def __init__(self, length):
        self.table = [[' ' for _ in range(length)] for _ in range(length)]
        self.h = length
        self.w = length

    def isSecure(self, x, y):
        return (self.h > x >= 0) and (self.w > y >= 0) and (self.table[x][y] == ' ')

    def update(self, x, y, player):
        self.table[x][y] = player.label

    def printTable(self):

        for ligne in self.table:
            new_ligne = '|'+''.join([ele+'|' for ele in ligne])
            print(new_ligne)

    def isFull(self):
        for array in self.table:
            if ' ' in array:
                return False
        return True

    def randomPlay(self, player):
        emptyCase = [(x, y) for x in range(self.h) for y in range(self.w) if self.table[x][y] == ' ']
        x, y = random.choice(emptyCase)
        print(f"L'ordinateur vient de mettre le pion sur la case ligne {x + 1} colonne {y + 1}")
        self.table[x][y] = player.label

    def computerPlay(self, player1, player2):
        liste_players = [player1, player2]
        for player in liste_players:

            liste_ran = random.sample(range(self.h), self.h)
            for i in range(self.h):
                if (self.table[i].count(player.label) == self.h - 1) and (' ' in self.table[i]):
                    index = self.table[i].index(' ')
                    print(
                        f"L'ordinateur vient de mettre le pion sur la case ligne {i + 1} colonne {index + 1}")
                    self.table[i][index] = player1.label

                    return

            liste_ran = random.sample(range(self.w),self.w)
            for j in liste_ran:
                colonnes = [row[j] for row in self.table]

                if (colonnes.count(player.label) == self.h - 1) and (' ' in colonnes):
                    index = colonnes.index(' ')
                    print(
                        f"L'ordinateur vient de mettre le pion sur la case ligne {index + 1} colonne {j + 1}")
                    self.table[index][j] = player1.label
                    return

            diagonal1 = [self.table[x][y] for x in range(self.h) for y in range(self.w) if x + y == (self.h - 1)]
            if (diagonal1.count(player.label) == self.h - 1) and (' ' in diagonal1):
                index = diagonal1.index(' ')
                print(f"L'ordinateur vient de mettre le pion sur la case ligne {index +1} colonne {self.h  - index}")
                self.table[index][self.h - 1 - index] = player1.label
                return

            diagonal2 = [self.table[x][y] for x in range(self.h) for y in range(self.w) if x == y]
            if (diagonal2.count(player.label) == self.h - 1) and (' ' in diagonal2):
                index = diagonal2.index(' ')
                print(f"L'ordinateur vient de mettre le pion sur la case ligne {index + 1} colonne {index +1}")
                self.table[index][index] = player1.label
                return
            
        self.randomPlay(player1)

    def isWin(self, joueurs):
        for joueur in joueurs:
            for i in range(self.h):
                if (self.table[i].count(joueur.label) == self.h):
                    return joueur

            for j in range(self.w):
                if ([row[j] for row in self.table].count(joueur.label) == self.w):
                    return joueur

            diagonal1 = [self.table[x][y] for x in range(self.h) for y in range(self.w) if x + y == (self.h - 1)]
            if (diagonal1.count(joueur.label) == self.h):
                return joueur

            diagonal2 = [self.table[x][y] for x in range(self.h) for y in range(self.w) if x == y]
            if (diagonal2.count(joueur.label) == self.h):
                return joueur

        return None


class Joueur:
    def __init__(self, name, label, isComputer=True):
        self.name = name
        self.label = label
        self.isComputer = isComputer

    def inputUser(self, message, morpion):
        while True:
            try:
                userInput = int(input(message))
            except ValueError:
                print("Veuillez entrer un nombre entre 1 et 3 ! Essayez encore.")
                continue
            if ((userInput < 1) | (userInput > morpion.h)):
                print("Veuillez entrer un nombre entre 1 et 3 ! Essayez encore.")
                continue
            else:
                return userInput
                break

    def inputCase(self, morpion):

        while True:
            x = self.inputUser("Veuillez entrer le numéro de la ligne", morpion)
            y = self.inputUser("Veuillez entrer le numéro de la colonne", morpion)
            if morpion.isSecure(x - 1, y - 1):
                morpion.update(x - 1, y - 1, self)
                print(f"Vous venez de mettre le pion sur la case ligne {x} colonne {y}")
                return
            else:
                print("La case est déjà remplie, merci de réessayer! ")


def play(morpion, players):
    while (morpion.isWin(players) is None) or (morpion.isFull() == False):

        liste_players = [[players[0], players[1]], [players[1], players[0]]]
        for joueurs in liste_players:
            morpion.printTable()

            if joueurs[0].isComputer == False:
                joueurs[0].inputCase(morpion)
            else:
                morpion.computerPlay(joueurs[0], joueurs[1])

            if morpion.isFull():
                morpion.printTable()
                print('Match null')
                return
            winner = morpion.isWin(players)
            if winner is not None:
                morpion.printTable()
                print(f'{winner.name}  a gagné')
                return

def main():
    morpion = Morpion(3)
    joueur1 = Joueur("Joueur 1", 'X', False)
    joueur2 = Joueur("Ordinateur", 'O', True)
    players = [joueur1, joueur2]
    play(morpion, players)

if __name__ == '__main__':
    main()

