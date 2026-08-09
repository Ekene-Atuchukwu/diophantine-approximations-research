import math
from fractions import Fraction

'''
Define a function that outputs a list (with maximum length specified) containing the partial quotients  of any real number x, including
floating-point precision issues and exact Fraction inputs
'''



def partial_quotients_generator(x, max_terms=15):
    """
    Computes the partial quotients [a0; a1, a2, ...] of a real number or Fraction x.
    Handles floating-point precision issues and exact Fraction inputs gracefully.
    """
    partial_quotients = []
    
    # 1. Exact rational arithmetic if x is a Fraction or int
    if isinstance(x, (Fraction, int)):
        num = x
        for terms in range(max_terms):
            a = num.numerator // num.denominator if isinstance(num, Fraction) else num
            partial_quotients.append(int(a))
            diff = num - a
            if diff == 0:
                break
            num = Fraction(num.denominator, num.numerator % num.denominator)
        return partial_quotients

    # 2. Float arithmetic with precision tolerance
    num = float(x)
    for _ in range(max_terms):
        # Snap to whole integer if floating-point drift is extremely small
        if abs(num - round(num)) < 1e-9:
            num = round(num)
            
        a = math.floor(num)
        partial_quotients.append(a)
        diff = num - a
        
        # Stop if the remainder is within tolerance of zero
        if math.isclose(diff, 0, abs_tol=1e-9):
            break
            
        num = 1.0 / diff
        
    return partial_quotients

def continued_fraction_representation(quotients, label):
    """
    Print a continued fraction in the standard math notation:
    [a0; a1, a2, a3, ...]
    """
    first = quotients[0]
    rest = quotients[1:]
    rest_text = ", ".join(str(n) for n in rest)
    print(label + " = [" + str(first) + "; " + rest_text + "]")

if __name__ == "__main__":

    print("FAMOUS IRRATIONAL NUMBERS (expansion repeats forever)")
    print("-" * 50)

    cf = partial_quotients_generator(math.sqrt(2))
    continued_fraction_representation(cf, "sqrt(2)")
    print("  (expected pattern: 1, then 2,2,2,2... forever)")
    print()

    golden_ratio = (1 + math.sqrt(5)) / 2
    cf = partial_quotients_generator(golden_ratio)
    continued_fraction_representation(cf, "golden ratio")
    print("  (expected pattern: all 1s forever)")
    print()

    cf = partial_quotients_generator(math.pi)
    continued_fraction_representation(cf, "pi")
    print()

    cf = partial_quotients_generator(math.e)
    continued_fraction_representation(cf, "e")
    print()
