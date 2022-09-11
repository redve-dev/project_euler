def find_sum(n):
    # the problem assumes integers in range [1, n)
    n=n-1
    num_of_3 = int(n/3)
    num_of_5 = int(n/5)
    num_of_15 = int(n/15)
    
    sum_of_3 = (2*3 + (num_of_3-1)*3)* (num_of_3/2)
    sum_of_5 = (2*5 + (num_of_5-1)*5)* (num_of_5/2)
    sum_of_15 = (2*15 + (num_of_15-1)*15)* (num_of_15/2)
    print(sum_of_3 + sum_of_5 - sum_of_15)

find_sum(1000)
