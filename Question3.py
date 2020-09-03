## Question3

import decimal

def sol(x,y,a,b):
    c= (x + (1/y))
    d= (x - (1/y))
    e=(y + (1/x) )
    f= (y - (1/x))
    num= decimal.Decimal(pow(c,a) * pow(d,b))
    den= decimal.Decimal(pow(e,a) * pow(f,b))
    s= num/den
    return float(s)

if __name__ == "__main__" :  
    x= float(input('Enter x:'))
    y= float(input('Enter y:'))
    a= float(input('Enter a:'))
    b= float(input('Enter b:'))
    print("Value after solving equation is", round(sol(x,y,a,b), 2)) 