# %% Partie 1 : classe individu 

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