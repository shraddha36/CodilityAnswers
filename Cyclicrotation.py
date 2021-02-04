def sol(A,K):
    if len(A)==0:
        return A
    K=K%len(A)
    return A[-K:]+A[:-K]

print(sol([1,2,3,4],2))
