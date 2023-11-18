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
            if i==p["y"] and j==p["x"]: 
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

m = [[0,0,0,1,1],
     [0,0,0,0,1],
     [1,1,0,0,0],
     [0,0,0,0,0]]
dico = {0:" ", 1:"#"}
p=create_perso((0,0))

print(display_map(m,dico))
print(create_perso((0,0)))
print(display_map_and_char(m,dico,p))

while True:
    lettre = input("Quel deplacement?")
    update = update_p(lettre,p)         
    print(display_map_and_char(m,dico,update))
     
    

    
        
        

    
