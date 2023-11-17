def display_map(m,d):
    for i in range(len(m)):
        for k in range(len(m[i])):
            for x,y in d.items():
                if m[i][k] == x:
                    m[i][k] = y
                    print(m[i][k], end='')
        print()
 
def display_map2(m, d):
    for row in m:
        for num in row:
            print(d[num], end='')
        print()

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
     
    

    
        
        

    