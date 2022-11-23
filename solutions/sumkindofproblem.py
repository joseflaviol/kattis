# https://open.kattis.com/problems/sumkindofproblem

def main():

    p = int(input())

    for i in range(p):
        k, n = input().split(" ")
        n = int(n)
        
        sum_all = 0
        sum_odd = 0
        sum_even = 0

        for j in range(1, n + 1):
            sum_all += j 
        
            if j % 2 == 0:
                sum_even += j
            else:
                sum_odd += j
        
        for j in range(n + 1, n * 2 + 1):
            if j % 2 == 0:
                sum_even += j
            else:
                sum_odd += j    
        
        print(k, sum_all, sum_odd, sum_even)

main()