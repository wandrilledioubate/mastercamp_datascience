

# %% Partie 1 : Le problème des 8 reines 

import random

echec_dim = 8

class individu:
    def __init__(self, val=None):
        if val is None:
            self.val = random.sample(range(echec_dim), echec_dim)
        else:
            self.val = val
        self.nbconflict = self.fitness()

    def __str__(self):
        return ' '.join(map(str, self.val))

    @staticmethod
    def conflict(p1, p2):
        # vérifie si les reines sont sur la même ligne, colonne ou diagonale
        return p1[0] == p2[0] or p1[1] == p2[1] or abs(p1[0] - p2[0]) == abs(p1[1] - p2[1])

    def fitness(self):
        self.nbconflict = 0
        for i in range(echec_dim):
            for j in range(i+1, echec_dim):
                if(individu.conflict([i, self.val[i]], [j, self.val[j]])):
                    self.nbconflict += 1
        return self.nbconflict


def create_rand_pop(count):
    return [individu() for _ in range(count)]


def evaluate(pop):
    return sorted(pop, key=lambda x: x.nbconflict)


def selection(pop, hcount, lcount):
    return pop[:hcount] + pop[-lcount:]


def croisement(ind1, ind2):
    new_ind1 = individu(ind1.val[:4] + ind2.val[4:])
    new_ind2 = individu(ind2.val[:4] + ind1.val[4:])
    return [new_ind1, new_ind2]


def mutation(ind):
    new_val = ind.val[:]
    index = random.randint(0, echec_dim - 1)
    new_val[index] = random.randint(0, echec_dim - 1)
    return individu(new_val)


def algoloopSimple():
    pop = create_rand_pop(25)  
    solution_trouvee = False
    nbr_iteration = 0

    while not solution_trouvee:  
        print("Iteration numéro : ", nbr_iteration)
        nbr_iteration += 1

        evaluation = evaluate(pop)  

        if evaluation[0].fitness() == 0:  
            solution_trouvee = True
        else:
            select = selection(evaluation, 10, 4)  
            croises = []
            
            for i in range(0, len(select), 2):  
                croises += croisement(select[i], select[i+1])

            mutes = []
            for i in select: 
                mutes.append(mutation(i))

            new_alea = create_rand_pop(5)  
            pop = select[:] + croises[:] + mutes[:] + new_alea[:]  

        print(evaluation[0])

# algoloopSimple()

# Non, le nombre d'itérations nécessaires est différent à  chaque lancement. 
# Plus de 4 milliards de combinaisons possibles donc approche de force brut inefficace

def algoloopAll():
    pop = create_rand_pop(25) 
    allsolutions = []
    nbriteration = 0
    while True: 
        nbriteration += 1
        evaluation = evaluate(pop) 
        
        if evaluation[0].fitness() == 0:
            if evaluation[0].val not in [sol.val for sol in allsolutions]:
                allsolutions.append(evaluation[0])
                print(f'Solution trouvée : {evaluation[0].val}')
                print(f'Nombre total de solutions trouvées : {len(allsolutions)}')
            
            evaluation.pop(0)
                
        if not evaluation: 
            pop = create_rand_pop(25)
            continue
        
        select = selection(evaluation, 10, 4) 
        croises = []
        
        for i in range(0, len(select), 2):
            croises += croisement(select[i], select[i+1])
            
        mutes = []
        for i in select:
            mutes.append(mutation(i))
        newalea = create_rand_pop(5)
        pop = select[:] + croises[:] + mutes[:] + newalea[:]
        
algoloopAll()


# %% Partie 2 : Cadre applicatif Numpy  
    

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Création d'un tableau 500 x 3 et remplissage avec nombres aléatoires distribués selon une loi normale centrée réduite

data = np.random.randn(500, 3)

# Affichage dans un scatter plot 3D 

fig = plt.figure(figsize=(10,10))

axis = fig.add_subplot(111, projection='3d')
axis.scatter(data[:,0], data[:,1], data[:,2], c=data[:,0],cmap='plasma')

plt.show()
 

# Moyenne de la colonne 0 

def mean_column_0(tab):
    mean_0 = np.mean(data[:, 0])
    print("La moyenne de la colonne 0 est de ",mean_0)


# Moyenne de chaque colonne

def mean_any_column(tab,col):
    mean_x = np.mean(tab[:, col])
    print("La moyenne de la colonne " + str(col) + " est de ",mean_x)


# Calcul de l'écart-type de la colonne 0 

def std_column_0(tab):
    std_0 = np.std(data[:, 0])
    print("L'écart-type de la colonne 0 est de ",std_0)

# Calcul de l'écart-type de chaque colonne

def std_any_column(tab,col):
    std_x = np.std(tab[:, col])
    print("L'écart-type de la colonne " + str(col) + " est de ",std_x)

"""

mean_column_0 = data[:, 0].mean()
std_column_0 = data[:, 0].std()

allmean_column = data.mean(axis = 0)
allstd_column = data.std(axis=0)

data_nor = (data-allmean_column)/(allstd_column)
"""

# Fonction pour normaliser les données
def normalisation(data):
    mean_all_cols = np.mean(data, axis=0)
    std_all_cols = np.std(data, axis=0)
    return (data - mean_all_cols) / std_all_cols

# Normaliser les données
datanorm = normalisation(data)

# Calculer la transposée de datanorm
datanorm_transpose = datanorm.T

# Calculer le produit matriciel de la transposée de datanorm par datanorm
covariance = np.dot(datanorm_transpose, datanorm)

# Verifier que le calcul de covariance est correct
np_covariance = np.cov(datanorm.T)
print("La matrice de covariance est-elle équivalente à np.cov ? ", np.allclose(covariance/499, np_covariance))

# Calculer les valeurs propres et les vecteurs propres
eigvals, eigvecs = np.linalg.eig(covariance)

# Triez les vecteurs propres en fonction de l’ordre décroissant des valeurs propres
idx = np.argsort(eigvals)[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

# Créer une matrice pca contenant les deux premières colonnes de la matrice de vecteurs propres triés
pca = eigvecs[:, :2]

# Project data
projecteddata = np.dot(datanorm, pca)

# Tracer les données
plt.figure(figsize=(10, 7))
plt.scatter(projecteddata[:, 0], projecteddata[:, 1], edgecolor='k', alpha=0.6)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Projection des données normalisées sur les deux premiers axes principaux')
plt.show()

print(projecteddata)

print(datanorm.shape)
print(pca.shape)

# Test des fonctions 

mean_column_0(data)
mean_any_column(data, 0)
std_column_0(data)
std_any_column(data,2)




## DISCUSSION 
# L'idée principale de la PCA est de transformer un ensemble de variables possiblement corrélées en un ensemble plus petit de variables non corrélées, appelées composantes principales.
# Cela peut permettre de : réduire la dimensionnalité, visualiser les données ou supprimer le bruit. 
# Dans notre cas, dans un algorithme génétique, cela sert à réduire la complexité de l'espace de recherche et aussi potentiellement de visualiser la progression de l'algorithme. 

# Les algorithmes génétiques sont une technique de recherche heuristique inspirée par le processus de sélection naturelle et de l'évolution selon les principes de la génétique et la théorie de Darwin. Ils sont souvent utilisés pour résoudre des problèmes d'optimisation et de recherche pour lesquels il n'existe pas de solution directe.

# Voici comment un algorithme génétique fonctionne typiquement :
    # 1. Initialisation : Création d'une population initiale d'individus. Chaque individu représente une solution possible au problème à résoudre.
    # 2. Évaluation : Chaque individu est évalué selon une fonction de fitness (ou de coût), qui mesure à quel point l'individu est une bonne solution au problème.
    # 3. Sélection : Des individus sont sélectionnés pour être les parents de la prochaine génération. Les individus ayant une meilleure fitness ont une plus grande chance d'être sélectionnés.
    # 4. Croisement (Crossover) : De nouveaux individus sont créés en combinant les traits de deux parents. Cela peut se faire de différentes manières, par exemple en prenant une partie de l'un parent et une partie de l'autre parent.
    # 5. Mutation : Les nouveaux individus sont légèrement modifiés aléatoirement. Cela permet d'introduire de la diversité dans la population et d'éviter de rester bloqué dans des optimums locaux.
    # 6. Nouvelle génération : La nouvelle population d'individus, qui est de la même taille que l'ancienne, remplace l'ancienne population. On retourne ensuite à l'étape 2, et le processus se répète jusqu'à ce qu'un critère d'arrêt soit atteint (par exemple, un certain nombre de générations ont été créées, ou une solution suffisamment bonne a été trouvée).

# Les algorithmes génétiques peuvent être utilisés pour résoudre une grande variété de problèmes, en particulier ceux pour lesquels il n'existe pas de solution exacte ou où la solution exacte serait trop coûteuse à calculer. Ils sont souvent utilisés pour résoudre des problèmes d'optimisation combinatoire, comme le problème du voyageur de commerce, le problème du sac à dos, ou la planification d'horaires.


