#!/usr/bin/env python3
import random
from player import *

DISCORD_CONNECTION = False
NUMBER_OF_VIRUS = 2

class Game:
    def __init__(self):
        self.list_of_players=[] #Contient les noms Discord des joueurs
        self.list_of_virus_roles=["virus"] #Hardcode, roles qui sont du Virus 
        self.list_of_service_roles=["service"] #Hardcode, roles qui sont du Service
        self.roles_dict={} #Reference le role attribue a chaque joueur
        self.players_dict={} #Contient les objets joueurs et leur numero (cle) permettant de les identifier

    def get_players(self):
        #TODO recup les joueurs depuis Discord
        if DISCORD_CONNECTION == False:
            self.list_of_players=["Joueur1#0001","Joueur2#0002","Joueur3#0003","Joueur4#0004","Joueur5#0005","Joueur6#0006"]

    def role_attribution(self):

        values = []
        keys = []

        virus_draw = [] #roles en jeu cote Virus
        service_draw = [] #roles en jeu cote Service


        for k in range(0,NUMBER_OF_VIRUS):
            index = random.randrange(0,len(self.list_of_virus_roles))
            virus_draw.append(self.list_of_virus_roles[index])

        for k in range(0,len(self.list_of_players)-NUMBER_OF_VIRUS):
            index = random.randrange(0,len(self.list_of_service_roles))
            service_draw.append(self.list_of_service_roles[index])

        values = virus_draw + service_draw #roles en jeu dans la partie

        random.shuffle(values) #randomisation
        print(values)

        keys = range(0,len(self.list_of_players)) #generation des cles joueur correspondantes
        print(keys)
        self.roles_dict = dict(zip(keys,values)) #attribution des roles aux joueurs

    def players_generation(self):
        for k in range(0,len(self.list_of_players)):
            name = self.list_of_players[k]
            ID = k
            role = self.roles_dict[k] 

            new_player = Player(name,ID,role)

            self.players_dict[k]=new_player



if __name__ == "__main__":

    mah_game = Game()
    mah_game.get_players()
    mah_game.role_attribution()
    print(mah_game.roles_dict)

    mah_game.players_generation()
    #for key in mah_game.players_dict:
    #    print(mah_game.players_dict[key].spec_dict)
    #    print(mah_game.players_dict[key].name)


