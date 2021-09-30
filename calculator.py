def add(x,y):
    return x+y
    
def subtract(x,y):
    return x-y
    
def multiply(x,y):
    return x*y
    
def divide(x,y):
    return x/y
    
print('What do you want to do?')
print('Addition')
print('subtraction')
print('multiplication')
print('division')

while True:
    choice=imput('Choose (1,2,3,4):')
    
    if choice in('1','2','3','4'):
        num1 = float('Type first number: ')
        num2 = float('Type second number: ')
        
        if choice == '1':
            print(num1, '+', num2 '=', add(num1, num2))
            
        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))
            
        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
            
        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
            
        next_math = imput('Want to do another one? (y/n)')
        if next_math = 'n':
            break
        
    else:
        print('invalid')
