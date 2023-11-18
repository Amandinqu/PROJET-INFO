def display_map(m,d):
    for ligne in m: # parcours la liste de la matrice 
        for elem in ligne: # parcours élément de la ligne associée
            print(d[elem], end="") # affiche la valeur associé de la matrice sans retour à la ligne avec "end" 
        print() # retour à la ligne 

def create_perso(depart):
    x,y = depart
    p={} # création du dictionnaire 
    p=["char"]="o" 
    p["x"] = x # si cle "x" n'existe pas, on l'ajoute au diccionaire avec la valeur x 
    p["y"] = y 
    return p

def display_map_and_char(m,d,p):
    x,y = p
    M = m.copy()#cf td 1 avec la methode copy
    for i,ligne in enumerate(M): 
        for j,valeur in enumerate(ligne): 
            if i==p["y"] and j==p["x"]: #y correspond aux lignes de la matrice et x aux valeurs de la matrice (sous-liste)
                print(p["char"],end" ") 
            else: 
                print(d[valeur],end" ")
            print()
            
def update_p(letter,p):
    if lettre in ["z","s","d","q"]:
        if lettre == "z":
            personne["y"] +=1
        if lettre == "s":
            personne["y"] -=1
        if lettre == "d":
            personne["x"] +=1
        if lettre == "q":
            personne["x"] -=1
    return personne

#proposition pour les ameliorations 3.1, 3.2:
def update_p(lettre,p,m): #changement de cordonnes en dicctionnaire de personnage
    if lettre in ["z","s","d","q"]:
        if lettre == "z": 
            p["y"] -=1 
            if p["y"] < 0 or m[p["y"]][p["x"]] == 1: #l'indice de "y" ne peut pas etre plus petite que la nombre des lignes de la matrice et si la valeur de matrice des cordonnees de notre x,y est egal a 1, on a #  
                p["y"] += 1     
        if lettre == "s":
            p["y"] +=1 
            if p["y"] >= len(m) or m[p["y"]][p["x"]] == 1: #l'indice de "y" ne peut pas etre plus grande que la nombre des lignes de la matrice
                p["y"] -= 1     
        if lettre == "d":  
            p["x"] +=1
            if p["x"] >= len(m[p["y"]]) or m[p["y"]][p["x"]] == 1: #l'indice de "x" ne peut pas etre plus grande que la nombre des colonnes de la matrice
                p["x"] -= 1      
        if lettre == "q":
            p["x"] -=1
            if p["x"] < 0 or m[p["y"]][p["x"]] == 1: #l'indice de "x" ne peut pas etre plus petite que la nombre des colonnes de la matrice
                p["x"] += 1               
    return p

m = [[0,0,0,1,1],
     [0,0,0,0,1],
     [1,1,0,0,0],
     [0,0,0,0,0]]
dico = {0:" ", 1:"#"}
p=create_perso((0,0))

print(display_map(m,dico)) #on a none a la fin a cause de print
print(create_perso((0,0)))
display_map_and_char(m,dico,p) #quand on n'utilise pas le print(display_map...) on n'a pas de none

while True:
    lettre = input("Quel deplacement?")
    update = update_p(lettre,p)         
    display_map_and_char(m,dico,update) #quand on n'utilise pas le print(display_map...) on n'a pas de none
    #2.4 comment arreter?
    

    
        
        

    
