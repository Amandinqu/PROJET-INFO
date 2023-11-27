import random # la génération de nombre aléatoires 

def display_map(m,d): # affichage de la carte 
    for ligne in m: # parcours la liste de la matrice 
        for elem in ligne: # parcours éléments de la ligne associée
            print(d[elem], end="") # affiche la valeur associé de la matrice sans retour à la ligne avec "end" 
        print() # retour à la ligne 
    
def generate_random_map(size_map,proportion_wall):
    M_generate = [[0 for elem in range(size_map)] for ligne in range(size_map)]
    nombre_mur = int(size_map*proportion_wall)
    nb = 0
    while nb < nombre_mur:
        x = random.randint(0,len(M_generate[0])-1) #on a -1 car en random la deuxieme caractere est inclu
        y = random.randint(0,len(M_generate)-1)
        if M_generate[y][x] == 0:
            M_generate[y][x] = 1 #on change la valeur de la matrice pour pouvoir utiliser la dictionaire avec la valeur qui correspond a objet
            nb += 1   
                    
    while M_generate[y][x]==0:
        x = random.randint(0, len(M_generate[0])-1)
        y = random.randint(0, len(M_generate)-1)
    M_generate[y][x] = 2
    
    while M_generate[y][x]==0:
        x = random.randint(0, len(M_generate[0])-1)
        y = random.randint(0, len(M_generate)-1)
     M_generate[y][x] = 3

    #entree_x=random.randint(0,len(M_generate[0])-1)
    #entree_y=random.randint(0,len(M_generate)-1)
    #while M_generate[entree_y][entree_x] != 0:
        #entree_x=random.randint(0,len(M_generate[0])-1)
        #entree_y=random.randint(0,len(M_generate)-1)
        
    #M_generate[entree_y][entree_x]=2 # represente l'entre par un 2 dans notre matrice
        
    #sortie_x=random.randint(0,len(M_generate[0])-1)
    #sortie_y=random.randint(0,len(M_generate[0])-1)
    #while M_generate[sortie_y][sortie_x]!=0 : 
        #sortie_x = random.randint(0, len(M_generate[0]) - 1)
        #sortie_y = random.randint(0, len(M_generate) - 1)
        
    #M_generate[sortie_y][sortie_x]=3

    return M_generate

def delete_all_walls(m,pos):
    (x,y)=pos
    # 8 cases entourant le personnage on peut utiliser une boucle imbriquée
    # le personnage est dans une matrice de taille 3*3 où le perso est sur la 9 ème case 
    for i in range(y-1,y+2): # parcours les positions -1,0 et 1 (y correspond aux lignes)
        for j in range(x-1,x+2): # parcours les position -1,0 et 1 
            if m[i][j]==1: # verifier si c'est un mur
                m[i][j]=0 # elève le mur

def create_perso(depart): # création dictionnaire représentant le personnage 
    x,y = depart # création du couple 
    p={} # création du dictionnaire 
    p["char"]="o" #on peut faire p = {"char":"o"}
    p["x"] = x # si cle "x" n'existe pas on crée la cle et on ajoute au dictionnaire avec la valeur x qui est sa position en abscisse 
    p["y"] = y # de même pour la position en ordonné
    p["score"] = 0 #initialisation du score pour avoir le score (3.6)
    return p

#proposition pour les ameliorations 3.1, 3.2:
def update_p(lettre,p,m): #changement de cordonnes en dictionnaire de personnage # ne sort pas de la carte 
    if lettre in ["z","s","d","q","E"]: #verification de la lettre entrée 
        if lettre == "z": # en haut 
            p["y"] -=1 # decremente de 1 "y" la position en ordonnée 
            if p["y"] < 0 or m[p["y"]][p["x"]] == 1: #l'indice de "y" ne peut pas etre plus petite que la nombre des lignes de la matrice et si la valeur de matrice des cordonnees de notre x,y est egal a 1, on a #  
                p["y"] += 1   # pour revenir dans la map 
        if lettre == "s": # en bas 
            p["y"] +=1 # incrémente de 1 "y" la position en ordonnée 
            if p["y"] >= len(m) or m[p["y"]][p["x"]] == 1: #l'indice de "y" ne peut pas etre plus grande que la longueur du nombre des lignes de la matrice si 
                p["y"] -= 1    # 
        if lettre == "d":  # à droite 
            p["x"] +=1
            if p["x"] >= len(m[p["y"]]) or m[p["y"]][p["x"]] == 1: #l'indice de "x" ne peut pas etre plus grande que la nombre des colonnes de la matrice
                p["x"] -= 1      
        if lettre == "q": #à gauche 
            p["x"] -=1
            if p["x"] < 0 or m[p["y"]][p["x"]] == 1: #l'indice de "x" ne peut pas etre plus petite que la nombre des colonnes de la matrice
                p["x"] += 1 
        if letter.upper()=="E": #marche aussi sans upper()
            delete_all_walls(m,(p["x"],p["y"])) 
    return p 

#proposition pour les ameliorations 3.4, 3.5
#premiere idee pour la creation des objets: on ajoute au dictionnaire d[2]="*" et on cree des objets par la modification de la matrice
def create_objects(nb_objects, m): 
    nb = 0 #nombre des objects on veut afficher
    while nb < nb_objects:
        x = random.randint(0,len(m[[0]])-1) #on a -1 car en random la deuxieme caractere est inclu len(m[0]) longueur de la première sous liste 
        y = random.randint(0,len(m)-1)
        if m[y][x] == 0:
            m[y][x] = 2 #on change la valeur de la matrice pour pouvoir utiliser la dictionaire avec la valeur qui correspond a objet
            nb += 1 # ajout pour que la boucle s'arrete 
            
def update_objects(p,objects):
    if m[p["y"]][p["x"]] == 2:  
        m[p["y"]][p["x"]] = 0 #pour que le score "mange une seule fois"
        p["score"] += 1 #ajout du score changement de score 
        
#create_object correct avec le sujet 
def create_objects(nb_objects, m):   
    objects_couple=set() #création d'un set vide 
    while len(objects_couple) < nb_objects: 
        x = random.randint(0,len(m[0])-1) #on a -1 car en random la deuxieme caractere est inclu
        y = random.randint(0,len(m)-1) 
        if m[y][x] == 0 and (x,y) not in objects_couple::
                objects_couple.add((x,y))
    return objects_couple
    
def update_objects(p,objects): #j'ai voulu supprimer des elements directement mais ca change le largeur d'ensemble alors derrange la boucle for, il faut creer un nouvel ensemble
    objects_copy = objects.copy()
    for x,y in objects_copy:
        if (p["x"], p["y"]) == (x,y):
            objects.remove((x,y))
            p["score"] += 1
    return objects

def display_map_and_char_and_objects(m, d, p, objects):
    M = m.copy()
    for i, ligne in enumerate(M):
        for j, valeur in enumerate(ligne):
            if i == p["y"] and j == p["x"]: #y correspond aux lignes de la matrice et x aux valeurs de la matrice (sous-liste)
                print(p["char"], end='')
            else:
                print(d[valeur], end='')
                
        print()
    print("your score: ", p["score"])  
#fin de premiere idee

def display_map_and_char(m,d,p): # affichage du personnage sur la carte en fonction de la position du perso et pour les autres la valeur du dictionnaire d
    x,y = p 
    M = m.copy()#cf td 1 avec la methode copy les modifications n'impactent pas la matrice d'origine 
    for i,ligne in enumerate(M): 
        for j,valeur in enumerate(ligne): # boucle imbriqué --> on parcourt ici chaque élément de la matrice M 
            if i==p["y"] and j==p["x"]: #y correspond aux lignes de la matrice et x aux valeurs de la matrice (sous-liste) 
                print(p["char"],end=" ") # affichage du personnage 
            else: 
                print(d[valeur],end=" ") # sinon on affiche la valeur du dic d 
            print() # retour à la ligne à la fin de chaque ligne de la matrice 
            
def display_map_and_char_object(m, d, p, objects):
    M = m.copy()
    for i, ligne in enumerate(M):
        for j, valeur in enumerate(ligne):
            if i == p["y"] and j == p["x"]: #y correspond aux lignes de la matrice et x aux valeurs de la matrice (sous-liste)
                print(p["char"], end='') # affichage du personnage 
            else:
            k = 0  # pour voir si on affiche etoile ou valeur du dictionnaire   
                for x,y in objects:
                    if i == y and j == x:
                        k +=1
                if k == 0:
                    print(d[valeur], end='')
                else:   
                    print("*", end="")
        print()
    print("your score: ", p["score"])

def create_new_level(p,m,objects,size_map, proportion_wall):
        new_objects = objects.copy() #il faut definir car si if n'est pas satisait il renvoie rien comme l'objets(mais pourquoi il n'est pas necessaire de definir m?)
        if m[p["y"]][p["x"]] == 3:
            M=generate_random_map(size_map,proportion_wall) # appel à la fonction
            m = M 
            for  i, ligne in enumerate(m):
                for j, valeur in enumerate(ligne):
                  if valeur == 2:  # 2 correpond à l'entree 
                      p["x"],p["y"] = j, i
            new_objects=create_objects(4,m)  # appel à la fonction
        return m, new_objects 


#ajout des bombes au code, cad des objets qu'on doit eviter car si on les touche, on perde le jeu (boucle while s'arrete)
def create_bombes(nb_bombes, m, objects): #il faut ajouter la propriete objects car il y a la possibilite d'avoir bombes et objects a la meme position quand on cree un nouvel niveau
    bombes_couple=set() #création d'un set vide 
    while len(bombes_couple) < nb_bombes: 
        a = random.randint(0,len(m[0])-1) #on a -1 car en random la deuxieme caractere est inclu
        b = random.randint(0,len(m)-1) 
        if m[b][a] == 0 and (a,b) not in bombes_couple and (a,b) not in objects: #pour ne pas avoir des objets et des bombes a la meme position
                bombes_couple.add((a,b))
    print(bombes_couple)
    return bombes_couple

def update_bombes(p,bombes): #j'ai voulu supprimer des elements directement mais ca change le largeur d'une ensemble alors derrange la boucle for, il faut creer une nouvelle ensemble
    bombes_copy = bombes.copy()
    for a,b in bombes_copy:
        if (p["x"], p["y"]) == (a,b): # si la personnage et a la position de la bombe on affiche le final score
            print()
            print("You lost :( your final score: ", p["score"])
            bombes = set() 
    return bombes   

def display_map_and_char_object_bombes(m, d, p, objects, bombes):
    M = m.copy()
    for i, ligne in enumerate(M):
        for j, valeur in enumerate(ligne):
            if i == p["y"] and j == p["x"]: #y correspond aux lignes de la matrice et x aux valeurs de la matrice (sous-liste)
                print(p["char"], end='')
            else:   
                k = 0
                for x,y in objects:
                    if i == y and j == x:
                        k +=1
                if k == 0: #on est sur qu'il n y a pas des objets a afficher, il faut verifier s'il ya des bombes
                    l = 0
                    for a,b in bombes:
                        if i == b and j == a:
                            l += 1
                    if l == 0:
                        print(d[valeur], end='')
                    else:
                        print("!", end="")
                else:
                    print("*", end="")
                
        print()
    print("your score: ", p["score"])

def create_new_level(p,m,objects,bombes,size_map, proportion_wall):
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

#print(display_map(m,dico)) #on a none a la fin a cause de print
size_map = 8
proportion_wall = 2
m = generate_random_map(size_map, proportion_wall)
create_perso((0,0))
objects = create_objects(4, m) # définir le nombre d'objet "*" dans notre jeu
#bombes = create_bombes(2, m, objects)
#display_map_and_char_object_bombes(m,dico,p, objects, bombes)
display_map_and_char_and_objects(m,dico,p,objects) #quand on n'utilise pas le print(display_map...) on n'a pas de none

while True:
    lettre = input("Quel deplacement?")
    updatep = update_p(lettre,p,m)  #changement coordonné de l'objet 
    m, objects = create_new_level(p,m,objects,size_map,proportion_wall)
    updateo = update_objects(p,objects) # effacer l'etoile 
    #updateb = update_bombes(p,bombes) #on verifie si la longeur de l'ensemble bombes doit changer
    #if len(updateb) == 0: #si oui, cad que la personnage a touche une bombe, le joueur perde
        #break #pour arreter la boucle
    #display_map_and_char_object_bombes(m,dico,updatep, updateo, updateb)
    display_map_and_char_and_objects(m,dico,updatep,updateo) #quand on n'utilise pas le print(display_map...) on n'a pas de none
    #2.4 comment arreter? # première idée dire que le nbr d'objet est égal au nbr d'objet "manger" par le personnage 




    

    
        
        

    
