"""
Main Script: Diophantine Approximation Suite
==============================================
This script brings together all three modules to run a
complete demonstration. Run this file to see everything
working together.
"""

import math
from module1_cf_generator import partial_quotients_generator, continued_fraction_representation
from module2_convergents import get_convergents, check_approximation_quality
from module3_spectrum import show_partial_quotients, approximation_difficulty


golden_ratio = (1 + math.sqrt(5)) / 2

print("DIOPHANTINE APPROXIMATION SUITE")
print("Author: Ekene Atuchukwu")
print()

print("STEP 1: Continued fraction of the golden ratio")
phi_quotients = partial_quotients_generator(golden_ratio)
continued_fraction_representation(phi_quotients, "golden ratio")
print()

print("STEP 2: Convergents and approximation quality")
check_approximation_quality(golden_ratio, phi_quotients, "golden ratio")
print()

print("STEP 3: How hard is the golden ratio to approximate?")
show_partial_quotients(phi_quotients, "golden ratio")
approximation_difficulty(golden_ratio, phi_quotients, "golden ratio")
