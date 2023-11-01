# Midterm 1 2023 Question 2
# Date: November 1st, 2023
import numpy as np
from midterm1 import linalg

def main():
    # define variables given in Q2
    a = 4.15e-2 # acceleration
    m = 3.68e4 # mass
    F = m * a # force
    E = 2.00e5 # Youngs' Modulus
    L = 2.75e3 # length of couplings between cars
    A = 2.25e4 # cross sectional area of couplings between cars
    k = E * A / L # stiffness parameter

    # coefficient matrix K (note that K has been normalized by k^5)
    K = np.array([
        [2, -2, 0, 0, 0],
        [-2, 3, -1, 0, 0],
        [0, -1, 2, -1, 0],
        [0, 0, -1, 3, -2],
        [0, 0, 0, -2, 2],
    ], 
    dtype = float,
    )
    print(f"Scaled Coefficient Matrix (K): \n{K}\n") # check coefficient matrix
    K_coeff = k * K # Non-normalized coefficient matrix
    print(f"Coefficient Matrix [K]: \n{K_coeff}\n")

    # Compute determinant of K to see if system has a unique solution
    det_K = np.linalg.det(K)
    print(f"The determinant of K: {det_K}\n")

    # Modified coefficient matrix (note that K1 has been normalized by k^4)
    K1 = np.array([
        [3, -1, 0, 0],
        [-1, 2, -1, 0],
        [0, -1, 3, -2],
        [0, 0, -2, 2],
    ], 
    dtype = float,
    )
    print(f"Scaled Modified Coefficient Matrix (K1): \n{K1}\n")
    #compute determinant of K1 to see if system has a unique solution
    det_K1 = np.linalg.det(K1)
    print(f"The determinant of K1: {det_K1}\n")

    # Check solution to Naive Gaussian Elimination
    F = np.array([F, 1.5 * F, F, 4 * F])
    print(f"Right-hand side vector, F: {F}\n")
    K2 = k * K1 # Multiply entire matrix by k to determine true displacements

    print(f"Coefficient matrix, (K2): \n{K2}\n") # Check new coefficient matrix
    u = linalg.solve(K2, F) # get unique solution to system
    print(f"Naive Gaussian Elimation solution of unknown displacements: {u}\n")

if __name__ == "__main__":
    main()