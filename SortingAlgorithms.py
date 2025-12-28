def min_max(A:list[float]) -> tuple[float, float]:
    """étapes de l'algorithme :
    1. diviser : diviser la liste en deux sous-listes de taille à peu près égale
    2. conquérir : trouver le minimum et le maximum de chaque sous-liste en utilisant la même fonction de manière récursive
    3. combine : comparer les minimums et maximums des deux sous-listes pour obtenir le minimum et le maximum de la liste entière
    
    le simple case : si la liste ne contient qu'un seul élément, le minimum et le maximum sont égaux à cet élément
    Ce qu'il se passe à l'étape 2 : la fonction est appelée récursivement sur les deux sous-listes jusqu'à ce que la taille de la liste soit réduite à 1 (le cas simple)


    """
    #simple cases
    print("appel de min_max sur la liste : ", A)
    if len(A) == 1:
        return A[0], A[0] 
    #divide
    n = len(A)//2
    #conquer
    min_left, max_left = min_max (A[:n])  # listes à gauche 
    min_right, max_right =  min_max(A[n:]) # listes à droite 
    #combine 
    return min(min_left,min_right), max(max_left, max_right)

A,B = min_max([1, 3, 2, 7, 4, 9, 8, 3])
print("minimum : ", A, "  maximum : ", B)


def quicksort(A):

    print("appel de quicksort sur la liste : ", A)
    if len(A) < 2:
        return A

    pivot = A[0]
    print("Le pivot est : ", pivot)
    low, high = [], []
    for i in range(1, len(A)):
        if A[i] <= pivot:
            low += [A[i]]
        else:
            high += [A[i]]

    low = quicksort(low)  # récursion sur la sous-liste des éléments plus petits que le pivot
    high = quicksort(high)  # récursion sur la sous-liste des éléments plus

    return low + [pivot] + high
    

A = quicksort([1, 2, 6, 5, 3, 7, 4])
print("quicksort result : ", A)


A = [1, 2, 6, 5, 3, 7, 4]

def peak_find(start: int = 0, end: int = len(A)):
    print(start, end)
    i = (start + end) // 2
    # simple case A[i] is max
    print("i : ", i)
    if A[i-1] < A[i] and A[i+1] < A[i]:
        return (i, A[i])

    #Divide
    elif A[i] < A[i-1]: #descente
        return peak_find(start, i)
    elif A[i] > A[i-1]: #montée
        return peak_find(i+1, end)


    return (i, A[i])

A = peak_find(end=len(A))
print("Peakfind : ", A)


def karatsuba(x, y):
    print("appel de karatsuba sur : ", x, y)
    # simple case
    if x < 10 or y < 10:
        return print("kara: ", x * y)
    # divide
    x_str = str(x)
    y_str = str(y)
    x_size = len(x_str)
    y_size = len(y_str)
    if x_size > 1:
        Xnew_x = int(x_str[:-x_size//2])  
        Xnew_y = int(x_str[-x_size//2:])  
        karatsuba(Xnew_x, Xnew_y)
    if y_size > 1:
        Ynew_x = int(y_str[:-y_size//2])  
        Ynew_y = int(y_str[-y_size//2:])  
        karatsuba(Ynew_x, Ynew_y)
    # conquer
    return None
    ac = first_x * first_y
    bd = second_x * second_y
    cross = x * y - ac - bd
    return  ac + cross + bd

print(karatsuba(34, 13))



def max_sum(A: list[float]) -> float:
    # simple case
    if len(A) < 2:
        return max(sum(A), 0)
    
    # divide
    n = len(A) // 2
    left_half = max_sum(A[:n])
    right_half = max_sum(A[n:])

    # conquer
    crossing = A[n]
    for i in [-1,1]:
        attempt = crossing
        for x in A[n+i:]:
            attempt += x
            crossing = max(crossing, attempt)
        for x in A[n-1::-i]:
            attempt += x
            crossing = max(crossing, attempt)

    return max(left_half, right_half, crossing)

A = [-2,1,-3,4,-1,2,1,-5,4]
print("max_sum : ", max_sum(A))