def derivative(n: int, m: int):
    lower,upper = (n*m),(m-1)
    if m == 1:
        print(str(lower) + 'x')
    elif m == 0:
        return 0
    else:
        print(str(lower) + 'x' + str(upper))
    # Second Derivative
    d2_dx = (lower*upper)
    print(d2_dx)
derivative(3,3)
