def knows(a, b, M):
    return M[a][b] == 1

def findCelebrity(n, M):
    stack = list(range(n))  

    while len(stack) > 1:
        person_a = stack.pop()  
        person_b = stack.pop()  

        if knows(person_a, person_b, M):
            stack.append(person_b)  
        else:
            stack.append(person_a)  
    if not stack:
        return -1 

    candidate = stack.pop()  
    for i in range(n):
        if i != candidate:  
            if knows(candidate, i, M) or not knows(i, candidate, M):
                return -1  
    return candidate  

M = [[0, 1, 1],  # Person 0 knows 1 and 2
     [0, 0, 1],  # Person 1 knows 2
     [0, 0, 0]]  # Person 2 knows nobody
n = len(M)  
print(findCelebrity(n, M))