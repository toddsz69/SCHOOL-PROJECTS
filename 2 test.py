def x(n):
    if n == 1:
        print("*")
    else:
        pattern = ["*" * (2 * n + 1)]
        for i in range(1, n):
            if i % 2 == 1:
                pattern.append("*" + "@" * (2 * n - 1) + "*")
            else:
                line = "*"
                for j in range(1, 2 * n):
                    if j % 2 == 1:
                        line += "@"
                    else:
                        line += "*"
                line += "*"
                pattern.append(line)
        
        pattern.append("*" * (2 * n + 1))
        
        for line in pattern:
            print(line)

n = int(input("Enter a number (1-20): "))
x(n)

