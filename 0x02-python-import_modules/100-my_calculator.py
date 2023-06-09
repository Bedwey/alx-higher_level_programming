#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    argvs = sys.argv
    argc = len(argvs)

    if (argc - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argvs[1])
    b = int(argvs[3])

    if argvs[2] == '+':
        print("{0} + {1} = {2}".format(a, b, calculator_1.add(a, b)))

    elif argvs[2] == '-':
        print("{0} - {1} = {2}".format(a, b, calculator_1.sub(a, b)))

    elif argvs[2] == '/':
        print("{0} / {1} = {2}".format(a, b, calculator_1.div(a, b)))

    elif argvs[2] == '*':
        print("{0} * {0} = {2}".format(a, b, calculator_1.mul(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
