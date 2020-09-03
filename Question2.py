## Question2

def fun(num) :  
    n= 0  
    if num % 2 == 0 : 
        n = (num * num) - 1;  
    else : 
        n = (num * num) + 1;  
    return n;  

if __name__ == "__main__" :  
    num = 9;  
    print(f"Next number of the series is {fun(num)}")  