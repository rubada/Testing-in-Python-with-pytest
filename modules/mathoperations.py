class MathOperations:

    @staticmethod
    def addition(*args):
        num = 0
        for i in args:
            num += i
        return num

    @staticmethod
    def subtraction(*args):
        # "num" should be equal to the first number in args
        num = args[0]
        # Starting the range with 1 to exclude the first number in args
        for i in range(1, len(args)):
            num = num - args[i]
        return num

    @staticmethod
    def multiplication(*args):
        num = args[0]
        for i in range(1, len(args)):
            num = num * args[i]
        return num

    @staticmethod
    def division(*args):
        try:
            return (args[0] / args[1])
        except ZeroDivisionError:
            raise ZeroDivisionError("The divisor shouldn't be zero")


if __name__ == "__main__":
    print(MathOperations.addition(1, 3))
    print(MathOperations.division(1, 0))
