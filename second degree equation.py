import matplotlib.pyplot


def roots(a, b, c):
    func = lambda x: (a*x**2) + (b*x) + c
    D = b**2 - 4*a*c
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)

    y_values = list()
    x_values = list()

    for x in range(-10, 10):
        y_values.append(func(x))
        x_values.append(x)

    print(x1)
    print(x2)

    matplotlib.pyplot.plot(x_values, y_values)
    matplotlib.pyplot.show()


"""roots(1, 2, 2)"""


