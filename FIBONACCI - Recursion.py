"""

@author: Akash Shah
Fibonacci Number, recursion practice
"""

def fibonacci(n):
    if n == 0: # This creates the first base case
        return(0)
    elif n == 1 or n == 2: # Creates the second base case 
        return(1)
    else:
        return(fibonacci(n-1) + fibonacci(n-2)) # Recursion, calculation for Fibonacci number

def main():
    n = int(input("How many numbers of Fibonacci do you want to print?: "))
    for i in range(1, n + 1): # Reads the 1 first ending at nth input
        print(fibonacci(i))

if(__name__ == "__main__"):
    main()


