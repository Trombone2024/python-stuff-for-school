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
    choice=input('Choose (+,-,*,/):')
    
    if choice in('+','-','*','/'):
        num1 = float(input('Type first number: '))
        num2 = float(input('Type second number: '))
        
        if choice == '+':
            print(num1, '+', num2, '=', add(num1, num2))
            
        elif choice == '-':
            print(num1, '-', num2, '=', subtract(num1, num2))
            
        elif choice == '*':
            print(num1, '*', num2, '=', multiply(num1, num2))
            
        elif choice == '/':
            print(num1, '/', num2, '=', divide(num1, num2))
            
        next_calculation = input('Want to do another one? (yes/no)')
        if next_calculation == 'no':
            break
        
    else:
        print('invalid')
