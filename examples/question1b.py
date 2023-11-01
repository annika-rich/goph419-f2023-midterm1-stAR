# Midterm 2023 Question 1

import numpy as np

def main():
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
    T = (L * (1 - a) ** 0.25) / (16 * np.pi * sigma * D ** 2) # Kelvins
    C = T - 272.15 # convert to Celsius
    print(f"The expected value of Earth's black body temperature (T) in Kelvin:  {T:0.10e}")
    print(f"The expected value of Earth's black body temperature (T) in Celsius: {C:0.10e}\n")

    # Total Error in T (plus contributions from errors in L, a, D)
    partial_L = (-L) / (64 * np.pi * ((1 -a) ** 0.75) * sigma * D ** 2)
    print(f"The error contributed by L: {np.abs(partial_L)}")

    partial_a = ((1 - a) ** 0.25) / (16 * np.pi * sigma * D ** 2)
    print(f"The error contributed by a: {np.abs(partial_a)}")

    partial_D = (-L * (1-a) ** 0.25) / (8 * np.pi * sigma * D ** 3)
    print(f"The error contributed by D: {np.abs(partial_D)}\n")

    total_error = np.abs(partial_L) * del_L + np.abs(partial_a) * del_a + np.abs(partial_D) * del_D
    relative_error = total_error / T # normalize error by true value
    print(f"Total error in T: {total_error:0.10e}")
    print(f"Relative error:   {relative_error:0.10e}")

    # Relative Error in T
    

if __name__ == "__main__":
    main()