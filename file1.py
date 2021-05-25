def sum_of_two(l,k):
    for i in range(len(l)-1):
            for j in range(i+1,len(l)):
                if l[i]+l[j] == k:
                    return(i,j)
     return 0           
