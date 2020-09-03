## Question1 (Method 1)

def sum(n,x): 
    s = 0.00  
    for i in range(1, n+1): 
        s += 1/x**i
    return s

if __name__ == "__main__" :  
    n = int(input('Enter value for n:'))
    x= float(input('Enter value for x:'))
    print("Sum is", round(sum(n,x), 2)) 



## Question1 (Method 2: USING RECURSION)

def sum(n): 
    if n == 0:
        return 0
    else:
        s = 1/x**n
        return (s + sum(n-1)) 

if __name__ == "__main__" :  
    n = int(input('Enter value for n:'))
    x= float(input('Enter value for x:'))
    print("Sum is", round(sum(n), 2)) 