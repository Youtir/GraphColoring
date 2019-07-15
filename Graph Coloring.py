#definition de fonctions
def merge(M,S):
    for i in range(len(S)):
        if S[i] not in M:
            M.append(S[i])
#Liste contenant des sous-listes de chaque sommet et son degré
print("Attention tout manque de rigueur et de précision en saisie des données pourra aboutir à des résultats non correctes")
d=int(input("Entrer le degré de votre graphe : "))
ga=[]
gd=[]
sc=[]
for i in range(d):
    S=input("Entrer le nom du sommet "+str(i+1))
    LSD=[S]
    LSA=[S]
    adjacent=input("entrer les noms des sommets adjacents à ce sommet séparés par un espace ")
    DS=len(adjacent.split())
    SA=adjacent.split()
    LSD.append(DS)
    LSA.append(SA)
    gd.append(LSD)
    ga.append(LSA)
#tri des deux listes de degrés et d'adjacence
na=len(ga)
nd=len(gd)
for i in range(na-1):
    for j in range(na-i-1):
        if len(ga[j][1])<len(ga[j+1][1]):
            ga[j],ga[j+1]=ga[j+1],ga[j]
for k in range(nd-1):
    for c in range(nd-k-1):
        if gd[c][1]<gd[c+1][1]:
            gd[c],gd[c+1]=gd[c+1],gd[c]
control=set()
for y in gd:
    sc.append([y[0],[]])
#association des couleurs
COLOR=0
STC=[]
for z in range(0,len(ga)):
    COLOR+=1
    CSA=ga[z][1]
    for v in range(z,len(ga)):
        if (ga[v][0] not in CSA) and (ga[v][0] not in STC):
            sc[v][1].append('COLOR'+str(COLOR))
            STC.append(ga[v][0])
            merge(CSA,ga[v][1])
print("la liste des sommets triés par ordre décroissant de leurs degrés est comme suit :",gd,sep='\n')
print("la coloration de votre graphe est représentée par la liste suivante :",sc,sep='\n')