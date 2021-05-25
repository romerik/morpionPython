#coding:utf-8
import os,time,random,sys

def affichage(tableau,player):
    os.system("clear")
    print("                                                         TOUR {}                                       \n\n".format(player))
    
    print("                  0                                        1                                2           ")
   
    print("     --------------------------------------------------------------------------------------------------------")
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("0    |            {}                        |              {}                    |              {}             |".format(tableau[0][0],tableau[0][1],tableau[0][2]))
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("     --------------------------------------------------------------------------------------------------------")
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("1    |            {}                        |              {}                    |              {}             |".format(tableau[1][0],tableau[1][1],tableau[1][2]))
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("     --------------------------------------------------------------------------------------------------------")
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("2    |            {}                        |              {}                    |              {}             |".format(tableau[2][0],tableau[2][1],tableau[2][2]))
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("     |                                     |                                   |                            |")
    print("     --------------------------------------------------------------------------------------------------------")

def verifie_Jeu_Terminer(tableau):
    if ((tableau[0][0]==tableau[0][1] and tableau[0][0]==tableau[0][2] and tableau[0][0]!="") or (tableau[1][0]==tableau[1][1] and tableau[0][0]==tableau[1][2] and tableau[1][0]!="") or (tableau[2][0]==tableau[2][1] and tableau[2][0]==tableau[2][2] and tableau[2][0]!="") or (tableau[0][0]==tableau[1][0] and tableau[0][0]==tableau[2][0] and tableau[0][0]!="") or (tableau[0][1]==tableau[1][1] and tableau[0][1]==tableau[2][1] and tableau[0][1]!="") or (tableau[0][2]==tableau[1][2] and tableau[0][2]==tableau[2][2] and tableau[0][2]!="") or (tableau[0][0]==tableau[1][1] and tableau[0][0]==tableau[2][2] and tableau[0][0]!="") or (tableau[0][2]==tableau[1][1] and tableau[0][2]==tableau[2][0] and tableau[0][2]!="")) or (tableau[0][0]!="" and tableau[0][1]!="" and tableau[0][2]!="" and tableau[1][0]!="" and tableau[1][1]!="" and tableau[1][2]!="" and tableau[2][0]!="" and tableau[2][1]!="" and tableau[2][2]!=""):
        print("\n\n ------------PARTIE TERMINER-------------")
        sys.exit()
    else:
        return 0
def ordi_Joue(tableau,caractere_ordi):
    joue,i=0,0
    while i<3:
        j=0
        while j<3:
            if tableau[i][j]=="" and joue==0:
                if j==0:
                    if tableau[i][j+1]==tableau[i][j+2] and tableau[i][j+1]!="":
                        tableau[i][j]=caractere_ordi
                        joue=1
                elif j==1:
                    if tableau[i][j-1]==tableau[i][j+1] and tableau[i][j-1]!="":
                        tableau[i][j]=caractere_ordi
                        joue=1
                else:
                    if tableau[i][j-1]==tableau[i][j-2] and tableau[i][j-1]!="":
                        tableau[i][j]=caractere_ordi
                        joue=1
            j+=1
        i+=1
    j=0
    while j<3:
        i=0
        while i<3:
            if tableau[i][j]=="" and joue==0:
                if i==0:
                    if tableau[i+1][j]==tableau[i+2][j] and tableau[i+1][j]!="":
                        tableau[i][j]=caractere_ordi
                        joue=1
                elif i==1:
                    if tableau[i-1][j]==tableau[i+1][j] and tableau[i-1][j]!="":
                        tableau[i][j]=caractere_ordi
                        joue=1
                else:
                    if tableau[i-1][j]==tableau[i-2][j] and tableau[i-1][j]!="":
                        tableau[i][j]=caractere_ordi
                        joue=1
            i+=1
        j+=1
    if joue==0:
        if tableau[0][0]==tableau[1][1] and tableau[0][0]!="" and tableau[2][2]=="":
            tableau[2][2]=caractere_ordi
            joue=1
        elif tableau[0][0]==tableau[2][2] and tableau[0][0]!="" and tableau[1][1]=="" and joue==0:
            tableau[1][1]=caractere_ordi
            joue=1
        elif tableau[1][1]==tableau[2][2] and tableau[1][1]!="" and tableau[0][0]=="" and joue==0:
            tableau[0][0]=caractere_ordi
            joue=1
        elif tableau[0][2]==tableau[1][1] and tableau[1][1]!="" and tableau[2][0]=="" and joue==0:
            tableau[2][0]=caractere_ordi
            joue=1
        elif tableau[0][2]==tableau[2][0] and tableau[1][1]=="" and tableau[2][0]!="" and joue==0:
            tableau[1][1]=caractere_ordi
            joue=1
        elif tableau[2][0]==tableau[1][1] and tableau[1][1]!="" and tableau[0][2]=="" and joue==0:
            tableau[0][2]=caractere_ordi
            joue=1
        else:
            while joue==0:
                ligne=random.randint(0,2)
                colonne=0
                while colonne<3 and joue==0:
                    if tableau[ligne][colonne]=="":
                        tableau[ligne][colonne]=caractere_ordi
                        joue=1
                    colonne+=1
                
    

print("------------{BIENVENUE DANS LE JEU DE MORPION}--------------")
tableauDeJeu=[["","",""],["","",""],["","",""]]
affichage(tableauDeJeu,"moi")
time.sleep(3)
os.system("clear")
print("Vous allez jouer contre l'ordinateur")
name_joueur=input("\n\nEntrer votre nom : ")
os.system("clear")
print("                                         LA PARTIE VA COMMENCER-                                         \n\n--------->Vous allez chaque fois entrer le numero de la ligne et celle de la colonne ou vous voulez jouer\n\n")
caractere_joueur=""
while caractere_joueur!='O' and caractere_joueur!='X':
    caractere_joueur=input("Choississez entre le caractere X et O pour pouvoir jouer: ")

if caractere_joueur=='X':
    caractere_ordi='O'
else:
    caractere_ordi='X'
time.sleep(1)

while not verifie_Jeu_Terminer(tableauDeJeu):
    ligneJoueur,colonneJoueur=5,5
    while ligneJoueur==5 or colonneJoueur==5:
        try: 
            ligneJoueur=int(input("Votre ligne: "))
            colonneJoueur=int(input("Votre colonne: "))
            if ligneJoueur<0 or ligneJoueur>2 or colonneJoueur<0 or colonneJoueur>2:
                raise ValueError("Mauvaise valeur")
            assert tableauDeJeu[ligneJoueur][colonneJoueur]==""
        except AssertionError:
            print("La case séléctionnée n'est pas vide")
            ligneJoueur,colonneJoueur=5,5
        except:
            print("------->Le numero de la ligne et de la colonne doivent etre des entier compris entre 0 inclus et 2 inclus\n")
            ligneJoueur,colonneJoueur=5,5
    tableauDeJeu[ligneJoueur][colonneJoueur]=caractere_joueur
    affichage(tableauDeJeu,name_joueur)
    verifie_Jeu_Terminer(tableauDeJeu)
    ordi_Joue(tableauDeJeu,caractere_ordi)
    affichage(tableauDeJeu,name_joueur)
    verifie_Jeu_Terminer(tableauDeJeu)

