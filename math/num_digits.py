import math

def num_digits(n):
    """
        num_digits(n) finds the number of digits in n
        parameters:
            n -> int
        returns:
            number of digits in n
    """

    digits=1+int(math.log10(n))
    return digits;

if(__name__ == "__main__"):
    n=10
    print(str(n)+" is a "+str(num_digits(10))+" digit number")