#K-Digit Chopping module with basic arithmatic

from decimal import Decimal

def chop(num,acc):
    
    num_str = '%E' % Decimal(str(num))
    exp=num_str[num_str.find("E")+1:]
    num_str=num_str[:num_str.find("E")-1]
    chop = float(num_str)
                    
    if float(chop)<0:
        chop = num_str[:acc+2]
    else:
        chop = num_str[:acc+1]
    
    num = float(chop)*10**int(exp)
    
    return num
    
def round(num,acc):
    
    num_str = '%E' % Decimal(str(num))
    exp=num_str[num_str.find("E")+1:]
    num_str=num_str[:num_str.find("E")-1]
    
    chop = float(num_str)
    
    if int(num_str[acc+2]) >= 5 and float(chop)<0.0:
        x = int(num_str[acc+1])
        x = x+1
        num_str = list(num_str)
        num_str[acc+1] = str(x)
    
        chop = num_str[:acc+2]
        chop = ''.join(chop)

    elif int(num_str[acc+1]) >= 5 and float(chop)>0.0:
        x = int(num_str[acc])
        x = x+1
        num_str = list(num_str)
        num_str[acc] = str(x)
        
        chop = num_str[:acc+1]
        chop = ''.join(chop)

    else:
        
        if float(chop)<0:
            chop = num_str[:acc+2]
        else:
            chop = num_str[:acc+1]

    num = float(chop)*10**int(exp)
    
    return num
    
def add(num1, num2, acc, method="round"):
    
    x = num1 + num2
    if method == "round":
        x = round(x,acc)
    else:
        x = chop(x,acc)
    
    return x

def subtract(num1, num2, acc, method="round"):
    
    x = num1 - num2
    if method == "round":
        x = round(x,acc)
    else:
        x = chop(x,acc)
    
    return x

def multiply(num1, num2, acc, method="round"):
    
    x = num1 * num2
    if method == "round":
        x = round(x,acc)
    else:
        x = chop(x,acc)
    
    return x

def divide(num1, num2, acc, method="round"):
    
    x = num1 + num2
    if method == "round":
        x = round(x,acc)
    else:
        x = chop(x,acc)
    
    return x

def factorial(num, acc, method = "round"):
    
    sum = 1        
        
    for i in range(1,num+1):
         sum = multiply(i,sum,acc,method)
         
    x = sum
    return x