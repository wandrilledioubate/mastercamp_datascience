# %% Exercice 1 

ch = "12 13 10 8 20"
my_list = list(map(int, ch.split()))
print(my_list)

# %% Exercice 2 

test = [1, 2, 3, 4, 6]
values1 = ['a', 'b', 'c', 'd', 'e']
values2 = ['A', 'B', 'C', 'D', 'E']

result = tuple(map(lambda x, y, z: y if x % 2 != 0 else z, test, values1, values2))
print(result)

# %% Exercice 3 

N = 2
my_list = [2 ** i for i in range(N)]
print(my_list)

# %% Exercice 4 

numbers=[-1,-2,-3,4,5,10,-5,3]

my_list = [x ** 2 for x in numbers if x < 0]
print(my_list)


# %% Exercice 5 

n = 14 
x = 2
my_list = [i for i in range(1,n) if i % x != 0]
print(my_list)


# %% Exercice 6

revert = ' '.join(sentence[::-1] for sentence in input("Entrez votre phrase: ").split())
print(revert)


# %% Exercice 7  

words = ' '.join(sentence for sentence in input("Entrez votre phrase: ").split() if sentence.islower() and sentence.isalpha())
print(words)

# %% Exercice 8 

s1 = "Kit Surf en Mer"
s2 = "Maison en Bois avec Surf"

s1_words = s1.lower().split()
s2_words = s2.lower().split()

common_words = set(s1_words) & set(s2_words)

s1 = ' '.join(word.upper() if word in common_words else word for word in s1_words)
s2 = ' '.join(word.upper() if word in common_words else word for word in s2_words)

print(s1)
print(s2)

# %% Exercice 9 

dico={'b':1, 'a':2, 'd':5}
revert_dico = {x: y for y, x in dico.items()} 
print(revert_dico)

# %% Exercice 10 

my_dict = {"a":"b", "b":"c", "c":"X"}
correspondances = {"a":"A", "b":"D", "c":"C"}
results = {k: correspondances[v] for k, v in my_dict.items() if v in correspondances}
print(results)


# %% Exercice 11 - A

def sortedList(liste):
    liste.sort()
    return liste 

# Test de la fonction 
l1=[5,3,10,4,8,20,2]
print(sortedList(l1))


# %% Exercice 11 - B

def sortedSizeWord(liste):
    liste.sort(key=lambda v: len(v))
    return liste

# Test de la fonction 
l2 = ["bonjour","tout","le","monde"]
print(sortedSizeWord(l2))


# %% Exercice 11 - C

def sortedDescMax(liste):
    liste.sort(key=max, reverse=True)
    return liste


# Test de la fonction 
l3 =[ [1,0,5],[1,2,3], [8,5] ]
print(sortedDescMax(l3))


# %% Exercice 11 - D

def sortedTuple(liste):
    liste.sort(key=lambda x: x[0])
    print("Liste triée par ordre alphabétique : ", liste)
    liste.sort(key=lambda x: x[1])
    print("Liste triée par âge : ", liste)   
    
# Test de la fonction 
l4=[('Luc',22),('Lea',18),('Alice',23),('Luca',21), ('Max',20) ]
print(sortedTuple(l4))

# %% Exercice 12 

def boomerang(iterable):
    items = list(iterable)
    yield from items
    yield from reversed(items)

# Test de la fonction 
l = [1, 2, 3]
for x in boomerang(l):
    print(x)
    
# %% Partie 2 - A 

# %% Partie 2 - A 

# Le constructeur de la classe est la méthode __init__. Cette méthode est appelée lorsqu'un nouvel objet est créé à partir de la classe. Dans cette classe, le constructeur prend quatre paramètres : self, nomClient, iban et solde.

# Les variables d'instances sont celles qui sont définies à l'intérieur du constructeur et qui sont précédées de self. Ces variables ont des valeurs différentes pour chaque instance de la classe. Dans cette classe, les variables d'instance sont self.nomClient, self.solde, et self.iban.

# Les variables de classe sont des variables qui sont partagées par toutes les instances de la classe. Elles sont définies en dehors de toute méthode et ne sont pas précédées de self. Dans cette classe, la variable de classe est cb_count.

# La méthode __str__ a été définie pour cette classe, ce qui permet l'utilisation de print(c2). Lorsque vous utilisez print sur une instance de classe, Python appelle automatiquement la méthode __str__ de cette classe pour obtenir une représentation en chaîne de caractères de l'objet. Ici, cette méthode renvoie une chaîne de caractères qui indique le propriétaire du compte.

# La méthode __eq__ a été définie pour cette classe, ce qui permet le test ==. Cette méthode spécifie ce qui doit être comparé lorsque vous utilisez == pour comparer deux instances de la classe. Ici, cette méthode compare les numéros iban des deux comptes bancaires. Si les deux numéros iban sont identiques, alors == renverra True; sinon, il renverra False.




# %% Partie 2 - B 


class Point3D:
    def __init__(self, x, y, z):
        self.coordinates = (x, y, z)

    def __str__(self):
        return f"Point3D({self.coordinates[0]}, {self.coordinates[1]}, {self.coordinates[2]})"

    def __abs__(self):
        return (self.coordinates[0] ** 2 + self.coordinates[1] ** 2 + self.coordinates[2] ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Point3D):
            x = self.coordinates[0] + other.coordinates[0]
            y = self.coordinates[1] + other.coordinates[1]
            z = self.coordinates[2] + other.coordinates[2]
            return Point3D(x, y, z)
        else:
            raise TypeError("L'opération d'addition n'est pas prise en charge pour les types fournis.")

    def __sub__(self, other):
        if isinstance(other, Point3D):
            x = self.coordinates[0] - other.coordinates[0]
            y = self.coordinates[1] - other.coordinates[1]
            z = self.coordinates[2] - other.coordinates[2]
            return Point3D(x, y, z)
        else:
            raise TypeError("L'opération de soustraction n'est pas prise en charge pour les types fournis.")

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.coordinates == other.coordinates
        else:
            return False

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = self.coordinates[0] * other
            y = self.coordinates[1] * other
            z = self.coordinates[2] * other
            return Point3D(x, y, z)
        elif isinstance(other, Point3D):
            x = self.coordinates[1] * other.coordinates[2] - self.coordinates[2] * other.coordinates[1]
            y = self.coordinates[2] * other.coordinates[0] - self.coordinates[0] * other.coordinates[2]
            z = self.coordinates[0] * other.coordinates[1] - self.coordinates[1] * other.coordinates[0]
            return Point3D(x, y, z)
        else:
            raise TypeError("L'opération de multiplication n'est pas prise en charge pour les types fournis.")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __setitem__(self, index, value):
        new_coordinates = list(self.coordinates)
        new_coordinates[index] = value
        self.coordinates = tuple(new_coordinates)

# Test de la classe Point3D
p1 = Point3D(1, 2, 3)
p2 = Point3D(4, 5, 6)

print(p1)  
print(p2)

distance = abs(p1 - p2)
print(distance)  

p3 = p1 + p2
print(p3)  

p4 = p2 - p1
print(p4) 

print(p1 == p2)  

p5 = p1 * 2
print(p5) 

p6 = p1 * p2
print(p6) 

p1[0] = 10
print(p1) 


# %% Partie 2 - C


class Mass3D(Point3D):
    def __init__(self, x, y, z, m):
        super().__init__(x, y, z)
        self.mass = m

    def __str__(self):
        return f"Mass3D({self.coordinates[0]}, {self.coordinates[1]}, {self.coordinates[2]}, {self.mass})"

# Test de la classe Mass3D  
mass_point = Mass3D(1, 2, 3, 10)
print(mass_point)  # Affiche Mass3D(1, 2, 3, 10)
    
  
m1 = Mass3D(1, 2, 3, 10)
m2 = Mass3D(4, 5, 6, 5)

print(m1) 
print(m2) 

distance_m = abs(m1 - m2)
print(distance_m)  

m3 = m1 + m2
print(m3) 

m4 = m2 - m1
print(m4) 

print(m1 == m2)  

m5 = m1 * 2
print(m5)

m6 = m1 * m2
print(m6)  

m1[0] = 10
print(m1)  
