# %% Exercice  1 : calcul de la vitesse

temps = 6.892
distance= 19.7

vitesse = distance / temps 
print("La vitesse est de", vitesse)

vitesse_2dec = "{:.2f}".format(vitesse)
print("La vitesse est de", vitesse_2dec)



# %% Exercice 2 - A : test à une alternative 

a = 10
b = 5

if a > b:
    maximum = a
    minimum = b
else:
    maximum = b
    minimum = a

print("Le maximum est :", maximum)
print("Le minimum est :", minimum)    



# %% Exercice 2 - B : test simple


a = 10
b = 5

maximum = a
minimum = b

if b > a:
    maximum = b
    minimum = a

print("Le maximum est :", maximum)
print("Le minimum est :", minimum)


# %% Exercice 2 - C : test ternaire

a = 22 
b = 46

maximum = a if a > b else b
minimum = a if a < b else b

print("Le maximum est :", maximum)
print("Le minimum est :", minimum)
    

# %% Exercice 3 

def volBoite(x1=None, x2=None, x3=None):
    if x1 is None:
        return None  

    if x2 is None and x3 is None:
        return x1 ** 3  

    if x2 is not None and x3 is None:
        return x1 ** 2 * x2  

    if x2 is not None and x3 is not None:
        return x1 * x2 * x3  

    return None    
    
# Test de la fonction
print (volBoite())
print (volBoite(5.2))
print (volBoite(5.2, 3))
print (volBoite(5.2, 3, 7.4))

# %% Exercice 4 

def eleMax(liste, debut=None, fin=None):
    if debut is None:
        debut = 0
    if fin is None:
        fin = len(liste) - 1
    
    max_element = liste[debut]
    for i in range(debut + 1, fin + 1):
        if liste[i] > max_element:
            max_element = liste[i]
    
    return max_element


# Test de la fonction 
serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]

print(eleMax(serie))
print(eleMax(serie, 2, 5))
print(eleMax(serie, 2))
print(eleMax(serie, fin =3, debut =1))

# %% Exercice 5 

def mixList(list1, list2):
    t3 = []
    min_length = min(len(list1), len(list2))
    
    for i in range(min_length):
        t3.append(list2[i])
        t3.append(list1[i])

    if len(list1) > len(list2):
        t3.extend(list1[min_length:])
    elif len(list2) > len(list1):
        t3.extend(list2[min_length:])
    
    return t3
    
# Test de la fonction 
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

print (mixList(t1, t2))

# %% Exercice 6 

def reverseList(chaine):
    reverse = chaine[::-1]
    return reverse

# Test de la fonction 
mot = 'fdnsfjdsnk'

print(reverseList(mot))

# %% Exercice 7 


def mafonction(arr): 
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)

# Test de la fonction
array = [1,8,8,2,9,3,10,5]
print(mafonction(array))                
                
# %% Exercice 8 

def countdown(start):
    for i in range(start, 0, -1):
        print(i, end=' ')
    print("GO!")
    
# Test de la fonction    
nb = 3
countdown(nb)

# %% Exercice 9 

def isPalindrome(word):
    word = word.replace(" ", "")
    reversed_word = word[::-1]
    if word == reversed_word:
        print(f"The word '{word}' is a palindrome.")
    else:
        print(f"The word '{word}' is not a palindrome.")


#Test de la fonction 
test = 'kayak'
isPalindrome(test)
    
# %% Exercice 10 

my_list = [0, 1, 2, 3, 4]
l1 = my_list + my_list[::-1]
l2 = my_list[:3] * 3
l3 = [my_list[i] for i in range(len(my_list)) if i % 3 == 0]

print("l1:", l1)
print("l2:", l2)
print("l3:", l3)

# %% Exercice 11 

x = int(input("Enter an integer: "))

if x % 2 == 0:
    print("pair")
else:
    print("impair")

# %% Exercice 12 

phrase = input("Enter a phrase: ")

words = phrase.split()
acronym = ""
for word in words:
    acronym += word[0].upper()

print(acronym)

# %% Exercice 13 

chaine = input("Enter a string: ")
c = input("Enter a character: ")

count = chaine.count(c)

print(f"'{c}' apparaît {count} fois dans \"{chaine}\"")

# %% Exercice 14 

def vowelCount(string):
    string = string.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

mot = 'maison'
vowelCount(mot)

# %% Exercice 15 

my_dict = {
    "pi": 3.14,
    "mot": "mot",
    "nombre": 42,
    "liste": [1, 2, 3]
}

print(my_dict["pi"])  
print(my_dict["mot"])  
print(my_dict["nombre"])  
print(my_dict["liste"])  

# %% Exercice 16 

my_dict = {
    "pi": 3.14,
    "mot": "mot",
    "nombre": 42,
    "liste": [1, 2, 3]
}

word = input("Enter a word: ")

if word in my_dict:
    value = my_dict[word]
    print(f"{word} vaut {value} dans my_dict")
else:
    print(f"{word} n'est pas une clé de my_dict")
    
    
# %% Exercice 17 

my_dict = {
    "pi": 3.14,
    "mot": "mot",
    "nombre": 42,
    "liste": [1, 2, 3]
}

my_dict["hello"] = "world"
my_dict["nombre"] = 0
del my_dict["pi"]

print(my_dict)


# %% Exercice 18 

values = [10, 20, 30, 40, 10, 2, 40]

s1 = {1, 2, 3}
s2 = set("Hello World")
s3 = set(values)
s4 = set(range(5, 16))

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)

