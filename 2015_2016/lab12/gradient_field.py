from random import choice
from collections import defaultdict

def contained(a, b):
    return all((v in b for v in a))

def free_face(K):
    for s1 in K:
        cofaces = [s for s in K if len(s) == len(s1) + 1 and contained(s1, s)]
        if len(cofaces) == 1: 
            return s1, cofaces[0]
    return None, None

def top_simplex(K):
    max_length = max([len(s) for s in K])
    return choice([s for s in K if len(s) == max_length])
                
def generate_field(K):
    K1, C, V = set(K), [], dict()
    while K1:
        s1, s2 = free_face(K1)
        if s1:
            V[s1] = s2
            K1.remove(s1)
            K1.remove(s2)            
        else:
            s = top_simplex(K1)
            C.append(s)
            K1.remove(s)
    return V, C
