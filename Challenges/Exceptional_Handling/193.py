# Simple calculator

class InvalidFormulaException(Exception):
    pass
def evaluate(formula):
    f = formula.split()
    if len(f) < 3:
        raise InvalidFormulaException('Formula should be have space')
    if f[1] == '+' or f[1] == '-' or f[1] == '*' or f[1] == '/':
        op1 = int(f[0])
        op2 = int(f[2])
        if f[1] == '+':
            res = op1+op2
        elif f[1] == '-':
            res = op1-op2
        elif f[1] == '*':
            res = op1*op2
        else: 
            res = op1/op2
        return res
    else:
        raise InvalidFormulaException ('invalidFormulaError: formula should be like this eg:op1 + op2')
formula = input('Enter the formula:')
try:
    # formula = input('Enter the formula:')
    print(evaluate(formula))
   
except InvalidFormulaException as e:
    print (e)


    

