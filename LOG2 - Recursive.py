"""

@author: Akash Shah
Log2 Function
"""
def log2(n):
    # Base Cases below
    if(n == 1 or n == 0):
        return(0)
    elif(n == 2):
        return(1)
    
    return(1 + log2(n//2))

n = 11 # Just an example
print(log2(n))
