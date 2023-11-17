def display_map(m,d):
    for ligne in m: # parcours la liste de la matrice 
        for elem in ligne: # parcours élément de la ligne associée
            print(d[elem], end="") # affiche la valeur associé de la matrice sans retour à la ligne avec "end" 
        print() # retour à la ligne 

def create_perso(depart):
    x,y = depart
    d = {"char": "o"}
    d["x"] = x # si cle "x" n'existe pas, on l'ajoute au diccionaire avec la valeur x 
    d["y"] = y 
    return d

def display_map_and_char(m,d,p):
    x,y = p
    M = m.copy()#cf td 1 avec la methode copy
    for i,ligne in enumerate(M): 
        for j,valeur in enumerate(ligne): 
            if i==p["y"] and j==p["x"]: 
                print(p["char"],end" ") 
            else: 
                print(d[valeur],end" ")
            print()
            
def update_p(letter,p):
    personne = create_perso(p)
    lettre = input("Quel deplacement?")
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

m = [[0,0,0,1,1],
     [0,0,0,0,1],
     [1,1,0,0,0],
     [0,0,0,0,0]]
dico = {0:" ", 1:"#"}
personnage=create_perso((0,0))
print(display_map(m,dico))
print(create_perso((0,0)))
print(display_map_and_char(m,dico,p))

lettre = input("Quel deplacement?")
print(display_map_and_char(m,dico,update_p(lettre,t)))
     
    

    
        
        

    
