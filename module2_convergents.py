"""
Module 2: Convergent Calculator
=================================
This file calculates convergents (rational approximations)
from a continued fraction, and checks how good each
approximation is.
"""

import math


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

def check_approximation_quality(true_value, partial_quotients, label):
    """
    For each convergent p/q of a real number x, check:
      1. How close p/q is to x (the error)
      2. Whether it beats Dirichlet's bound: error < 1/q^2

    Dirichlet's theorem guarantees infinitely many
    convergents will satisfy this bound. In practice, for
    continued fraction convergents, almost every single one
    satisfies it.
    """
    
    convergents = get_convergents(partial_quotients)
    print("Approximation quality for", label)
    print(f"{'n':<3} {'p/q':<10} {'decimal':<12} {'error':<12} {'1/q^2':<12} {'beats bound?'}")
    print("-" * 65)
    
    for n in range(len(convergents)):
        p, q = convergents[n]
        decimal_value = p / q
        error = abs(true_value - decimal_value)
        bound = 1 / (q * q)
        beats_bound = error < bound
        
        fraction_str = f"{p}/{q}"
        print(f"{n:<3} {fraction_str:<10} {decimal_value:<12.4f} {error:<12.8f} {bound:<12.8f} {str(beats_bound)}")

if __name__ == "__main__":
    golden_ratio = (1 + math.sqrt(5)) / 2
    phi_partial_quotients = [1]*10
    check_approximation_quality(golden_ratio, phi_partial_quotients, "golden ratio")
    print()

    sqrt2 = math.sqrt(2)
    sqrt2_partial_quotients = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    check_approximation_quality(sqrt2, sqrt2_partial_quotients, "square root of 2")
    print()

    pi = math.pi
    pi_partial_quotients = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 3, 3]
    check_approximation_quality(pi, pi_partial_quotients, "pi")
    print()

    e = math.e
    e_partial_quotients = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10]
    check_approximation_quality(e, e_partial_quotients, "Euler's number(e)")
    print()
