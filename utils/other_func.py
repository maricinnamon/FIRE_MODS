import math
from utils.const import OPTIMIZATION, POPULATION




def euclidean_distance(a, b):
    """ EUCLIDEAN DISTANCE BETWEEN TWO POINTS """
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    # Евклідова відстань між точками
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d  


def s(X):
    """ SORT BY LAST VALUE (FITNES-FUCNCTION) """
    return X[-1]
 

def aggregate(P, comprG, turnBestG, turnCenterG):
    """ AGGREGATE ALL POPULATIONS """
    P_full = []
    P_full.extend(P)
    
    for i in range(len(comprG)):
       curFIG = comprG[i]
       P_full.extend(curFIG)
    
    for i in range(len(turnBestG)):
       curFIG = turnBestG[i]
       P_full.extend(curFIG)    
    
    for i in range(len(turnCenterG)):
       curFIG = turnCenterG[i]
       P_full.extend(curFIG) 
       
    if (OPTIMIZATION == "max"):
        P_full.sort(key = s, reverse = True)
    elif (OPTIMIZATION == "min"):
        P_full.sort(key = s, reverse = False)        
        
    return P_full


def delete_duplicates(X):
    """ DELETE DUPLICATES """
    unique =[]
    for elem in X:
        if elem not in unique:
            unique.append(elem)
    return unique  


def make_new_population(P_full):
    """ MAKE NEW POPULATION """
    P = P_full[:POPULATION]
    return P
