# This is a file containing functions for all the major equations (nunbered accordingly) in the paper; these can be copy-pasted for implementation
# Equation 1: Cardiac Action Potentials without Memoery
def eqn1(x_i, ts, n, A, B1, B2, T1, T2, DImin):
    result = A - B1*np.exp((x_i-n*ts)/T1) - B2*np.exp((x_i-n*ts)/T2)
    if result < DImin:
        result = DImin
    return(result)

# Equation 4: Cardiac action potentials with memory term a:
def eqn4(x_i, x_i1, ts, n, a, A, B1, B2, T1, T2, DImin):
    result = A - B1*np.exp(((x_i/a)-n*ts)/T1) - B2*np.exp(((x_i1/a)-n*ts)/T2)
    if result < DImin:
        result = DImin
    return(result)

# Equation 5.1: Fixed Points for Equation 4
def eqn5(n, ts, a, A, B1, T1, B2, T2, xmax):
    M = np.exp((-n*ts)/T1)
    N = np.exp((-n*ts)/T2)
    L = 1 + (xmax * B1 * M)/(a*T1) + (xmax * B2 * N)/(a * T2)
    result = (A - B1 * M - B2 * N)/L
    return(result)

