import Calculator


def simple_test():
    # Ask for input
    print("Please enter the first number: ")
    a = float(input())
    print("Please enter second number: ")
    b = float(input())
    print(f"Addition: {Calculator.add(a,b)}, Multiplication: {Calculator.mul(a, b)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simple_test()


