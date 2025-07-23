import numpy as np
import pandas as pd

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def main():
    np.random.seed(123)  
    N = 2000

    # 1) Generate A: Probability of being Liberal = pA
    pA = 0.4
    A = np.random.binomial(1, pA, size=N)

    # 2) Generate C (SES): Probability of Low SES is higher for Liberals
    #    P(C=1 | A=1) = 0.6, P(C=1 | A=0) = 0.3
    C = np.array([
        np.random.binomial(1, 0.6 if a==1 else 0.3)
        for a in A
    ])

    # 3) Generate M1 (community service hours).
    M1 = []
    for i in range(N):
        base = 3.0  # baseline hours
        if A[i] == 1:
            base += 2.0  # liberals do more volunteering
        if C[i] == 1:
            base -= 1.0  # low SES might reduce volunteering opportunities
        val = np.random.normal(base, 1.0)  # some noise
        M1.append(val)
    M1 = np.array(M1)

    # 4) Generate M2 (address = 1 if urban, 0 if rural).
    M2 = []
    for i in range(N):
        if A[i] == 1:
            p_urban = 0.7
        else:
            p_urban = 0.3
        if C[i] == 1:
            p_urban += 0.1
        p_urban = min(max(p_urban, 0), 1)
        M2.append(np.random.binomial(1, p_urban))
    M2 = np.array(M2)

    # 5) Generate Y (Hiring) using a logistic model
    beta0 = -1.0
    betaA = -0.8
    betaC = -1.5
    beta1 =  0.3
    beta2 =  0.2

    linpred = beta0 + betaA*A + betaC*C + beta1*M1 + beta2*M2
    prob = sigmoid(linpred)
    Y = np.random.binomial(1, prob)

    # Put into a DataFrame
    df = pd.DataFrame({
        'A': A,
        'C': C,
        'M1': M1,
        'M2': M2,
        'Y': Y
    })

    print(df.head(10))

if __name__ == "__main__":
    main()
