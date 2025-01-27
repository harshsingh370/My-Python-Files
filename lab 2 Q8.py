# Function to print the sequence
def print_series(n):
    a, b = 1, 1  
    print(a, end=" ")  
    
    for _ in range(n - 1):
        print(b, end=" ")  
        a, b = b, a + b  
print_series(7)
