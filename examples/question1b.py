# Midterm 2023 Question 1
# Date: Tuesday October 31st, 2023

import numpy as np

def main():
    "This script calculates and prints answers to Question 1 for Midterm 1, GOPH419, F2023"

    sigma = 6.670374419e-8 # Stefan-Boltzmann constant

    # Relative Error in Solar Luminosity, L
    L = 3.828e26
    del_L = 0.004e26
    error_L = del_L / L
    print(f"The relative error in solar luminosity (L):         {error_L:0.5e}")
    
    # Relative Error in albedo, a
    a = 0.306
    del_a = 0.001
    error_a = del_a / a
    print(f"The relative error in Earth's albedo (a):           {error_a:0.5e}")

    # Relative Error in orbital distance, D
    D = 1.496e11
    del_D = 0.025e11
    error_D = del_D / D
    print(f"The relative error in Earth's orbital distance (D): {error_D:0.5e}\n")

    # expected value of Earth's black body Temperature T
    partial_a = (-L) / (64 * np.pi * ((1 -a) ** 0.75) * sigma * D ** 2)
    partial_L = ((1 - a) ** 0.25) / (16 * np.pi * sigma * D ** 2)
    partial_D = (-L * (1-a) ** 0.25) / (8 * np.pi * sigma * D ** 3)

    # True value of T
    T_true = (L * (1 - a) ** 0.25) / (16 * np.pi * sigma * D ** 2) # Kelvins
    # 1st order Taylor Series Sum of T(xi +1)
    T = T_true + partial_L + partial_a + partial_D
    C = T - 272.15 # convert to Celsius
    print(f"The expected value of Earth's black body temperature (T) in Kelvin:  {T:0.10e}")
    print(f"The expected value of Earth's black body temperature (T) in Celsius: {C:0.10e}\n")

    # Total Error in T (plus contributions from errors in L, a, D)
    contr_L = np.abs(partial_L) * del_L
    print(f"The error contributed by L: {contr_L:0.5e}")

    contr_a = np.abs(partial_a) * del_a
    print(f"The error contributed by a: {contr_a:0.5e}")

    contr_D = np.abs(partial_D) * del_D
    print(f"The error contributed by D: {contr_D:0.5e}\n")

    total_error = contr_L + contr_a + contr_D
    relative_error = ((T_true - T) / T_true) * 100 # normalize error by true value
    print(f"Total error in T:          {total_error:0.10e}")
    print(f"Relative error (%):        {relative_error}")

if __name__ == "__main__":
    main()