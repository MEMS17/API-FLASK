import random

# equipe = {'nom' : 'PSG',

# 'position':'1'}

# print(equipe['nom'])


# l = [1,5,3]

# for n in l :
#     print(n)

# def somme(a,b):
#     return a+b

# print(somme(2,3))


def somme_r_randind():
    a=random.randint(0,100)
    b=random.randint(0,100)
    return {'a':a, 'b':b, 'a+b':a+b}

print(somme_r_randind())

def somme_r_choice():
    x=random.choice(range(0,100))
    y=random.choice([5,8,30,50])
    return {'x':x, 'y':y, 'x+y':x+y}
print(somme_r_choice())


def aleatoire(booleen, liste, min, max):
    if booleen == True :
        u=random.choice(liste)
        return u
    else :
        v=random.randint(min,max)
        return v

print(aleatoire(True, [10,15,18,17,14], 0, 100))
print(aleatoire(False,[],0,100))