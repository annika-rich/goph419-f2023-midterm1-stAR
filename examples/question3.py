# Midterm 1 2023 Question 3
# Date: November 1st, 2023
import numpy as np

def main():
    E = 2.00e5 # Youngs' Modulus
    L = 2.75e3 # length of couplings between cars
    A = 2.25e4 # cross sectional area of couplings between cars
    k = E * A / L # stiffness parameter
    # 3.b) Cholesky decomposition check
    K1 = np.array([
        [3, -1, 0, 0],
        [-1, 2, -1, 0],
        [0, -1, 3, -2],
        [0, 0, -2, 2],
    ], 
    dtype = float,
    )

    # Scale up matrix by k^4
    K = k * K1
    print(f"Coefficient matrix (K): \n{K}\n")

    K_transpose = np.transpose(K)
    print(f"Transpose of coefficient matrix (K^T): \n{K_transpose}\n")

    print("Therefore [K] = [K^T] and can be used for Cholesky decomposition.\n")

    #3 3.c) K^-1
    # compute the inverse of K
    inv = np.linalg.inv(K)
    print(f"The inverse matrix of K is:\n {inv}\n")

    # check if it's the inverse
    A = np.linalg.solve(K,inv)
    print(f"[K][K]^-1 = \n{A}\n")

    B = np.linalg.solve(inv, K)
    print(f"[K]^-1[K] = \n{A}\n")
    print("[K][K]^-1 = [K]^-1[K]\nTherefore, the correct inverse matrix of [K] was computed.\n")
    
    # Condition number using [K] and [K]^-1
    norm_K = np.linalg.norm(K)
    norm_inv = np.linalg.norm(inv)
    cn = norm_K * norm_inv
    print(f"Condition number of [K]: {cn}\n")

    # Check condition number of matrix K using the Frobenius norm
    con = np.linalg.cond(K, 'fro')
    print(f"Checking condition number of [K]: {con}\n")

    # compare to same size identity matrix [I]
    I = np.identity(4)

    cond_I = np.linalg.cond(I)
    print(f"The condition number of [I]: {cond_I}\n")

    print(f"The CN[K] ({cn}) >> CN[I] ({cond_I}).\nTherefore, the system is ill-conditioned and will magnify errors and uncertainty in [K].\n")
if __name__ == "__main__":
    main()