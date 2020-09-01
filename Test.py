from math import *


def println(var):
    print(var, end="\n")

def minmax(nb1, nb2):
    print("max =", max(nb1, nb2), end="\n")
    print("min =", min(nb1, nb2), end="\n")

def resultat(moy):
    if(moy<0):
        print("moyenne ne peut etre neg")
    elif(moy < 8):
        print('Recale')
    elif(moy < 10):
        print("rattrapage")
    elif(moy <= 20):
        print("admis")
    else:
        print("mauvaise moyenne")


def somme():
    sum = 0
    a = eval(input())
    while(a != 0 ):
        sum += a
        a=eval(input())
    println(sum)


def duree(h, m, s):
    print(h*3600+m*60+s, "secondes")


def convheure(time):
    seconde = time%60
    minute = time//60
    hours = time//3600
    print(hours,"h",minute,"min",seconde,"sec")

#convheure(int(input("Entrez secondes : ")))

def pairInTupleSeq(myTup):
    sum = 0
    for x in myTup:
        if(x%2 == 0):
            sum += 1
    println(sum)


#duree(2, 1, 1)
#myTup = {2, 5, 6, 7, 15, 16, 18}
#pairInTupleSeq(myTup)

def prod(nb, *args):

    for i,number in enumerate(args):
        nb *= number
    print(nb)

#prod(4,5,10)

def vowels(mytxt):
    vowel = {'a', 'e', 'i', 'o', 'u', 'y'}
    sum = 0
    mytup = tuple(mytxt)
    for x in mytup:
        if x in vowel:
            sum += 1
    print(sum)


vowels("je suis la")