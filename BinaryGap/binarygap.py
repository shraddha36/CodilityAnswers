def solution(N):
    b=bin(N).split('0b')
    b=b[1]
    count,count_check=0,0

    for i in b:
        
        if (i)=="0":
            count+=1
       

        else:
            if count_check<count:
                count_check=count
            
            count=0
    return count_check
print(solution(561892))