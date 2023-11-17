def display_map(m,d):
    for ligne in m: # parcours la liste de la matrice 
        for elem in ligne: # parcours élément de la ligne associée
            print(d[elem], end="") # affiche la valeur associé de la matrice sans retour à la ligne avec "end" 
        print() # retour à la ligne 

m = [[0,0,0,1,1],
     [0,0,0,0,1],
     [1,1,0,0,0],
     [0,0,0,0,0]]
dico = {0:" ", 1:"#"}  
print(display_map(m,dico))

def create_perso(depart):
    x,y = depart
    d = {"char": "o"}
    d["x"] = x # si cle "x" n'existe pas, on l'ajoute au diccionaire avec la valeur x 
    d["y"] = y 
    return d
print(create_perso((0,0)))


def display_map_and_char(m,d,p):
    x,y = p
    M = m.copy()#cf td 1 avec la methode copy
    personne = create_perso(p)
    M[x][y] = personne[char]
    map=display_map(M,d)
    
t = (0,0)   
print(display_map_and_char(m,dico,t))
     
    

    
        
        

    
