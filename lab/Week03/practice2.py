def isPass(a,b) -> bool:
    if a<40 or b<40:
        return False
    if a+b<110:
        return False
    
    return True
    