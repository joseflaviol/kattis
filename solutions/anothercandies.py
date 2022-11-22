# https://open.kattis.com/problems/anothercandies

def main():

    t = int(input())

    for i in range(t):
        input() # process blank line

        childrens = int(input())
        total_candies = 0
        for j in range(childrens):
            candies = int(input())
            total_candies += candies
        
        if total_candies % childrens == 0:
            print("YES")
        else:
            print("NO")

main()