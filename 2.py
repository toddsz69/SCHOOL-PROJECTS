def x(n): 
    if n == 1: 
        print("*") 
    elif n == 2: 
        pattern = [ 
            "***", 
            "*@*", 
            "***" 
            ] 
        for line in pattern: 
            print(line) 
    elif n == 3: 
        pattern = [ 
            "*****", 
            "*@@@*", 
            "*@*@*", 
            "*@@@*", 
            "*****" 
            ] 
        for line in pattern: 
            print(line) 
    else: 
        print("Pattern not defined for this input")  
        
n = int(input("Enter a number: ")) 
x(n)
