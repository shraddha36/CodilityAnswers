# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    lis=[]
    for i in range(len(P)):
        slice=S[P[i]:Q[i]+1]
        if "A" in slice:
            lis.append(1)
        elif "C" in slice:
            lis.append(2)
        elif "G" in slice:
            lis.append(3)
        elif "T" in slice:
            lis.append(4)
    return lis
