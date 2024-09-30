                                     
# calculaor
def add(n1,n2):
    return n1+n2

def sub (n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide (n1,n2):
    return n1/n2

operation={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide    
}

def calculator():
    num1=float(input("What's the first number"))
    for key in operation:
        print(key)
    should_continue=True
    while should_continue:
        operation_symbol=input("Choose an operator +,-,*,/:")
        num2=float(input("What's the second number"))
        calculation_function=operation[operation_symbol]
        answer=calculation_function(num1,num2)#note down when  a function  is called auto with dictionary then againa sign the value
        print(f"{num1}{operation_symbol}{num2}={answer}")
        if input("Type y to continue else too type n")=="y":
            num1=answer
        else:
            should_continue=False
            calculator() 
calculator()