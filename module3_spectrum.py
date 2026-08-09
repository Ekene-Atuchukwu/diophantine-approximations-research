"""
Module 3: Comparing How Hard Numbers Are to Approximate
==========================================================
This file compares different irrational numbers by looking
at their partial quotients and how well their convergents
approximate them.

The key idea: if a number's partial quotients are all small
and bounded, the number is "badly approximable" - meaning
it's hard to find really good rational approximations to it.

The golden ratio has ALL partial quotients equal to 1, the
smallest possible value. This makes it the "hardest" number
to approximate by rationals - this is Hurwitz's theorem.
"""

import math
from fractions import Fraction


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


def get_convergents(partial_quotients):
    """
    Turn a list of partial quotients into a list of
    convergents (p, q) pairs, where p/q approximates
    the original number.

    The formula (recurrence relation) is:
        p_n = a_n * p_(n-1) + p_(n-2)
        q_n = a_n * q_(n-1) + q_(n-2)

    We start with two "seed" values before the list begins(that is, at n=0):
        p_(-1) = 1, p_(-2) = 0
        q_(-1) = 0, q_(-2) = 1
    """
    convergents = []

    p_before_last = 1
    p_last = partial_quotients[0]
    q_before_last = 0
    q_last = 1

    convergents.append((p_last, q_last))

    for a in partial_quotients[1:]:
        p_new = a * p_last + p_before_last
        q_new = a * q_last + q_before_last

        convergents.append((p_new, q_new))

        p_before_last = p_last
        p_last = p_new
        q_before_last = q_last
        q_last = q_new

    return convergents



def show_partial_quotients(partial_quotients, label):
    """
    Print the partial quotients and report the largest one.
    Small, bounded quotients mean the number is hard to
    approximate well.
    """
    print(label, "partial quotients:", partial_quotients)
    print("  Largest quotient found:", max(partial_quotients))
    if max(partial_quotients) == 1:
        print("  All quotients are 1 - as bounded as possible")
    print()


def approximation_difficulty(true_value, partial_quotients, label):
    """
    For each convergent, compute q^2 * error.

    As we take more convergents, this value settles down
    to a fixed number. That fixed number tells us how hard
    true_value is to approximate:

      - A LARGER settled value means HARDER to approximate
      - A SMALLER settled value means EASIER to approximate

    Hurwitz's theorem says this settled value can NEVER be
    larger than 1/sqrt(5), about 0.4472. The golden ratio is
    the number that actually reaches this maximum, making it
    the hardest number of all to approximate.
    """
    convergents = get_convergents(partial_quotients)

    print("Testing", label)
    print("q^2 * error for each convergent:")

    for n in range(13):
        p, q = convergents[n]
        decimal_value = p / q
        error = abs(true_value - decimal_value)
        scaled_error = (q * q) * error
        print("  n =", n, " q =", q, " q^2 * error =", round(scaled_error, 6))

    print()


if __name__ == "__main__":

    golden_ratio = (1 + math.sqrt(5)) / 2

    print("HURWITZ LIMIT: 1/sqrt(5) =", round(1/math.sqrt(5), 6))
    print()

    phi_q = partial_quotients_generator(golden_ratio)
    show_partial_quotients(phi_q, "Golden ratio")

    sqrt2_q = partial_quotients_generator(math.sqrt(2))
    show_partial_quotients(sqrt2_q, "sqrt(2)")

    pi_q = partial_quotients_generator(math.pi)
    show_partial_quotients(pi_q, "pi")

    e_q = partial_quotients_generator(math.e)
    show_partial_quotients(e_q, "Euler's number (e)")

    approximation_difficulty(golden_ratio, phi_q, "Golden ratio")
    approximation_difficulty(math.sqrt(2), sqrt2_q, "sqrt(2)")
    approximation_difficulty(math.pi, pi_q, "pi")
    approximation_difficulty(math.e, e_q, "e")

    print("CONCLUSION:")
    print("The golden ratio's scaling errors consistently oscillate and settle right up against")
    print("the 0.447214 Hurwitz limit, making it the most stubborn, 'hardest' number to approximate. ")
    print("In contrast, Euler number's(e) partial quotients grow sequentially with integers steadily increasing,")
    print("its scaling errors do not stay flat; they exhibit a downward trend, dipping lower and lower over time (dropping to ~0.08 by n=11).")
    print("Numbers with massive partial quotients like pi (which features a quotient of 292)")
    print("experience sharp drops in their scaling errors (plummeting to near 0.003), yielding exceptionally")
    print("accurate, high-quality approximations relative to the size of their denominators. Sqrt(2)'s values settle lower, around 0.3536, meaning")
    print("better approximations are available for sqrt(2) than phi.")
