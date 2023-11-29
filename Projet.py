import random # la génération de nombre aléatoires 

def display_map(m,d): # affichage de la carte 
    for ligne in m: # parcours la liste de la matrice 
        for elem in ligne: # parcours éléments de la ligne associée
            print(d[elem], end="") # affiche la valeur dans le dictionnaire sans retour à la ligne avec "end" 
        print() # retour à la ligne 
    
def generate_random_map(size_map,proportion_wall): # génère une carte de manière alétoire 
    M_generate = [[0 for elem in range(size_map)] for ligne in range(size_map)] # création d'une matrice nulle 
    nombre_mur = int(size_map*proportion_wall) # calcul du nbr de mur sur la carte en le convertissant en un entier 
    nb = 0 
    while nb < nombre_mur: # boucle qui place les murs et s'arrête si le nbr de mur correspond au nbr demander 
        x = random.randint(0,len(M_generate[0])-1) #on a -1 car en random la deuxieme caractere est inclu 
        y = random.randint(0,len(M_generate)-1) # création de position aleatoire dans la matrice 
        if M_generate[y][x] == 0: # si la case est libre 
            M_generate[y][x] = 1 #on change la valeur de la matrice pour pouvoir utiliser la dictionaire avec la valeur qui correspond à objet (1:#)
            nb += 1  

    entree_x=random.randint(0,len(M_generate[0])-1)  # création de coordonnées aléatoires 
    entree_y=random.randint(0,len(M_generate)-1)
    while M_generate[entree_y][entree_x] != 0: # tant que la case de la matrice n'est pas libre on cree de nouveaux coordonnées jusqu'à trouver une case libre 
        entree_x=random.randint(0,len(M_generate[0])-1) 
        entree_y=random.randint(0,len(M_generate)-1)
        
    M_generate[entree_y][entree_x]=2 # represente l'entree par un 2 dans notre matrice
        
    sortie_x=random.randint(0,len(M_generate[0])-1) # création de coordonnées aléatoires 
    sortie_y=random.randint(0,len(M_generate[0])-1)
    while M_generate[sortie_y][sortie_x]!=0 : # tant que la case de la matrice n'est pas libre on cree de nouveaux coordonnées jusqu'à trouver une case libre 
        sortie_x = random.randint(0, len(M_generate[0]) - 1)
        sortie_y = random.randint(0, len(M_generate) - 1)
        
    M_generate[sortie_y][sortie_x]=3 # represente la sortie par un 3 dans notre matrice 
    
    return M_generate 
#premiere idee pour l'entree et la sortie
    #while M_generate[y][x]==0:
        #x = random.randint(0, len(M_generate[0])-1)
        #y = random.randint(0, len(M_generate)-1)
    #M_generate[y][x] = 2
    
    #while M_generate[y][x]==0:
        #x = random.randint(0, len(M_generate[0])-1)
        #y = random.randint(0, len(M_generate)-1)
     #M_generate[y][x] = 3 # lors de l'affichage on a remarque que ce code a remplace l'entree par la sortie 


def delete_all_walls(m,pos): # enlève les murs autour de la position pos
    (x,y)=pos # pos est un tuple 
    # idee : 8 cases entourant le personnage on peut utiliser une boucle imbriquée
    # le personnage est dans une matrice de taille 3*3 où le perso est sur la 9 ème case 
    for i in range(y-1,y+2): # parcours les positions -1,0 et 1 (y correspond aux lignes)
        for j in range(x-1,x+2): # parcours les position -1,0 et 1 
            if m[i][j]==1: # verifie si il y a un mur dans la case 
                m[i][j]=0 # elève le mur

def create_perso(depart): # création dictionnaire représentant le personnage 
    x,y = depart 
    p = {"char": "o", "x": x, "y": y, "score": 0} 
    return p
#premiere idee, mais trop long
    #x,y = depart # création du couple 
    #p={} # création du dictionnaire 
    #p["char"]="o" #on peut faire p = {"char":"o"}
    #p["x"] = x # si cle "x" n'existe pas on crée la cle et on ajoute au dictionnaire avec la valeur x qui est sa position en abscisse 
    #p["y"] = y # de même pour la position en ordonné
    #p["score"] = 0 #initialisation du score pour avoir le score (3.6)


#proposition pour les ameliorations 3.1, 3.2:
def update_p(lettre,p,m): #changement de cordonnes en dictionnaire de personnage # ne sort pas de la carte 
    if lettre in ["z","s","d","q","E"]: #verification de la lettre entrée 
        if lettre == "z": # deplace en haut 
            p["y"] -=1 # decremente de 1 coordonnée y du personnage 
            if p["y"] < 0 or m[p["y"]][p["x"]] == 1: # si coordonnée y est negative il sort de la carte (en haut) l'indice de "y" ne peut pas etre plus petite que le nombre des lignes de la matrice ou si le personnage rencontre un mur(1)  
                p["y"] += 1   # pour revenir dans la map
        if lettre == "s": # deplace en bas 
            p["y"] +=1 # incrémente de 1 "y" la position en ordonnée 
            if p["y"] >= len(m) or m[p["y"]][p["x"]] == 1: # si le l'indice de "y" ne peut pas etre plus grande que la longueur du nombre des lignes de la matrice sinon il sort de la carte en bas ou si le personnage rencontre un mur  
                p["y"] -= 1    # pour revenir dans la map 
        if lettre == "d":  # deplace à droite 
            p["x"] +=1 # incremente de 1 
            if p["x"] >= len(m[p["y"]]) or m[p["y"]][p["x"]] == 1: #si l'indice de "x" ne peut pas etre plus grande que la nombre des colonnes de la matrice sinon il sort de carte coté droit ou si le personnage rencontre un mur 
                p["x"] -= 1     # pour revenir dans la map  
        if lettre == "q": # deplace à gauche 
            p["x"] -=1 # decremente de 1 
            if p["x"] < 0 or m[p["y"]][p["x"]] == 1: #si l'indice de "x" ne peut pas etre plus petite que la nombre des colonnes de la matrice sinon il sort de la carte coté gauche ou si le personnage rencontre un mur 
                p["x"] += 1 # pour revenir dans la map 
        if letter=="E": 
            delete_all_walls(m,(p["x"],p["y"])) # appel à la fonction suppression des mur autour du perso 
    return p 

#proposition pour les ameliorations 3.4, 3.5
#premiere idee pour la creation des objets: on ajoute au dictionnaire d[2]="*" et on cree des objets par la modification de la matrice
def create_objects_idee(nb_objects, m): 
    nb = 0 #nombre des objects on veut afficher
    while nb < nb_objects:
        x = random.randint(0,len(m[[0]])-1) #on a -1 car en random la deuxieme caractere est inclu len(m[0]) longueur de la première sous liste 
        y = random.randint(0,len(m)-1)
        if m[y][x] == 0:
            m[y][x] = 2 #on change la valeur de la matrice pour pouvoir utiliser la dictionaire avec la valeur qui correspond a objet
            nb += 1 # ajout pour que la boucle s'arrete 
            
def update_objects_idee(p,objects):
    if m[p["y"]][p["x"]] == 2:  
        m[p["y"]][p["x"]] = 0 #pour que le score "mange une seule fois"
        p["score"] += 1 #ajout du score changement de score 
        
#create_object correct avec le sujet 
def create_objects(nb_objects, m):   
    objects_couple=set() #création d'un set vide 
    while len(objects_couple) < nb_objects: # tant le nbr d'element dans l'ensemble objects_couple inferieur à nbr d'objet demandé 
        x = random.randint(0,len(m[0])-1) # on a -1 car en random la deuxieme caractere est inclu
        y = random.randint(0,len(m)-1) # creation de manière aléatoire coordonnées 
        if m[y][x] == 0 and (x,y) not in objects_couple: # si la case est vide et le couple n'est pas encore dans ensemble objet couple 
                objects_couple.add((x,y)) # ajout du couple (coordonnées) dans l'ensemble 
    return objects_couple
    
def update_objects(p,objects): # ramassage de l'objet 
    if (p["x"], p["y"]) in objects: # si les coordonnées du personnage sont dejà dans l'ensemble des positions des objets 
        objects.remove((p["x"], p["y"])) # on enlève les coordonnees de l'objet 
        p["score"] += 1 
    return objects  
#premiere idee avec la copie
    #objects_copy = objects.copy()
    #for x,y in objects_copy:
        #if (p["x"], p["y"]) == (x,y):
            #objects.remove((x,y))
            #p["score"] += 1


def display_map_and_char(m,d,p): # affichage de la carte et de la position du personnage sur cette carte 
    x,y = p 
    M = m.copy()#cf td 1 avec la methode copy les modifications n'impactent pas la matrice d'origine 
    for i,ligne in enumerate(M): #boucle imbriquee parcourt element de la matrice et leur indice i 
        for j,valeur in enumerate(ligne): #parcourt chaque élément de la ligne et leur indice j
            if i==p["y"] and j==p["x"]: # si indices (i,j) sont égales aux positions du perso (y,x) 
                print(p["char"],end=" ") # affichage du personnage 
            else: 
                print(d[valeur],end=" ") # sinon on affiche la valeur du dictionnaire 
            print() # retour à la ligne à la fin de chaque ligne de la matrice 
            
def display_map_and_char_object(m, d, p, objects):
    M = m.copy()  # création d'une copie pour eviter les modifications sur la matrice d'origine 
    for i, ligne in enumerate(M): #boucle imbriquee parcourt element de la matrice et leur indice i 
        for j, valeur in enumerate(ligne): #parcourt chaque élément de la ligne et leur indice j
            if i == p["y"] and j == p["x"]:# si indices (i,j) sont égales aux positions du perso (y,x) 
                print(p["char"], end='') # affichage du personnage 
            elif (j,i) in objects: # coordonnées (j,i) sont égales aux coordonnées de l'ensemble objet 
                print("*", end="") # affiche l'objet sur la carte 
            else:
                print(d[valeur], end='') # sinon on affiche la valeur du dictionnaire 
         print() # retour à la ligne à la fin de chaque ligne de la matrice 
    print("your score: ", p["score"])
#premiere idee mais trop long
            #else:
            #k = 0  # pour voir si on affiche etoile ou valeur du dictionnaire   
                #for x,y in objects:
                    #if i == y and j == x:
                        #k +=1
                #if k == 0:
                    #print(d[valeur], end='')
                #else:   
                    #print("*", end="")
        #print()
    #print("your score: ", p["score"])

def create_new_level(p,m,objects,size_map, proportion_wall): # création d'un nouveau niveau 
        new_objects = objects.copy() # si la condition n'est pas satisfaite alors on ne renvoie rien et l'ensemble object ne sera pas impacter par les modifications 
        if m[p["y"]][p["x"]] == 3: # si coordonnées du perso est égale à la sortie 
            M=generate_random_map(size_map,proportion_wall) # appel à la fonction en créant un nouvelle carte 
            m = M # remplace la carte par une nouvelle 
            for  i, ligne in enumerate(m): # parcourt chaque element et l'indice i de la matrice m 
                for j, valeur in enumerate(ligne): # parcourt chaque élément de la ligne et leur indice j
                  if valeur == 2:  # 2 correpond à l'entree 
                      p["x"],p["y"] = j, i # mise à jour position du perso avec coordonnées de l'entrée 
            new_objects=create_objects(4,m)  # appel à la fonction 
        return m, new_objects 


#ajout personel: ajout des bombes cad des objets qu'on doit eviter car si on les touche, on perde le jeu (boucle while s'arrete)
def create_bombes(nb_bombes, m, objects): #il faut ajouter la propriete objects car il y a la possibilite d'avoir bombes et objects "*" à la meme position quand on cree un nouvel niveau
    bombes_couple=set() #création d'un set vide 
    while len(bombes_couple) < nb_bombes: # tant que le nbr de bombes est inferieur au nbr de bombes souhaitées 
        a = random.randint(0,len(m[0])-1) #on a -1 car en random la deuxieme caractere est inclu 
        b = random.randint(0,len(m)-1) # creation de manière aléatoire des coordonnées pour les bombes 
        if m[b][a] == 0 and (a,b) not in bombes_couple and (a,b) not in objects: #pour ne pas avoir des objets et des bombes à la meme position 
                bombes_couple.add((a,b)) # ajout du couple dans l'ensemble 
    print(bombes_couple)
    return bombes_couple

def update_bombes(p,bombes): # cela supprime les elements directement mais ça change le largeur d'un ensemble alors derange la boucle for, il faut creer une nouvelle ensemble
    if (p["x"], p["y"]) in bombes: # si le personnage et à la position de la bombe on affiche le final score
        print()
        print("You lost :( your final score: ", p["score"])
        bombes = set() 
    return bombes   

def display_map_and_char_object_bombes(m, d, p, objects, bombes):
    M = m.copy() # pour eviter les modification sur la matrice d'origine 
    for i, ligne in enumerate(M): 
        for j, valeur in enumerate(ligne):
            if i == p["y"] and j == p["x"]: #y correspond aux lignes de la matrice et x aux valeurs de la matrice (sous-liste)
                print(p["char"], end='') # affichage du perso 
            elif (j,i) in objects: 
                print("*", end="") # affichage des objets "*" 
            elif (j,i) in bombes: 
                print("!", end="")   # affichage des bombes "!" 
            else:
                print(d[valeur], end='') # sinon affichage valeur du dictionnaire 
                
        print()
    print("your score: ", p["score"])

def create_new_level2(p,m,objects,bombes,size_map, proportion_wall):
        new_objects = objects.copy() #on fait pas du copie car si le condtion if n'est pas satisfait, la fonction renvoie pas de valeur
        new_bombes = bombes.copy() 
        if m[p["y"]][p["x"]] == 3:
            M=generate_random_map(size_map,proportion_wall) # appel à la fonction
            m = M
            for  i, ligne in enumerate(m):
                for j, valeur in enumerate(ligne):
                  if valeur == 2:  # 2 correpond à l'entree 
                      p["x"],p["y"] = j, i
            new_objects=create_objects(4,m)  # appel à la fonction
            new_bombes=create_bombes(2,m,new_objects) 
        return m, new_objects, new_bombes


dico = {0:" ", 1:"#", 2:" ", 3:"X"} 
p=create_perso((0,0))

#print(display_map(m,dico)) #il y a un None à la fin à cause du print() 
size_map = 8
proportion_wall = 2
m = generate_random_map(size_map, proportion_wall)
create_perso((0,0))
objects = create_objects(4, m) # définir le nombre d'objet "*" dans notre jeu
display_map_and_char_and_objects(m,dico,p,objects) #quand on n'utilise pas le print(display_map...) on n'a pas de None 
bombes = create_bombes(2, m, objects)
display_map_and_char_object_bombes(m,dico,p, objects, bombes)

while True:
    lettre = input("Quel deplacement?")
    updatep = update_p(lettre,p,m)  #changement coordonné de l'objet 
    m, objects = create_new_level(p,m,objects,size_map,proportion_wall)
    updateo = update_objects(p,objects) # rammasage des etoiles
    display_map_and_char_and_objects(m,dico,updatep,updateo) #quand on n'utilise pas le print(display_map...) on n'a pas de none


#while avec ajout personel
while True:
    lettre = input("Quel deplacement?")
    updatep = update_p(lettre,p,m)  #changement coordonné de l'objet 
    m, objects = create_new_level(p,m,objects,size_map,proportion_wall)
    updateo = update_objects(p,objects) # effacer l'etoile 
    updateb = update_bombes(p,bombes) #on verifie si la longeur de l'ensemble bombes doit changer
    if len(updateb) == 0: #si oui, cad que la personnage a touche une bombe, le joueur perde
        break #pour arreter la boucle
    display_map_and_char_object_bombes(m,dico,updatep, updateo, updateb)
    display_map_and_char_and_objects(m,dico,updatep,updateo, updateb) #quand on n'utilise pas le print(display_map...) on n'a pas de none





    

    
        
        

    
