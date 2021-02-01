def solution(A):
    a=A[0]
    b=sum(A[1:])
    diff=abs(a-b)
    for i in range(1,len(A)-1):
        a+=A[i]
        b-=A[i]
        new_diff=abs(a-b)
        if diff>new_diff:
            diff=new_diff
    return diff
