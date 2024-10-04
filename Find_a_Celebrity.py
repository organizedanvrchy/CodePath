# LINK to Question: https://guides.codepath.org/compsci/Find-A-Celebrity

def findCelebrity(n: int) -> int:
    # Step 1: Find the potential celebrity
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    
    # Step 2: Verify if the candidate is actually a celebrity
    for i in range(n):
        if i != candidate:
            # A celebrity must be known by everyone and must not know anyone else
            if knows(candidate, i) or not knows(i, candidate):
                return -1
    
    return candidate
