# https://open.kattis.com/problems/kitten

def main():

    fathers = {}

    kitten_node = int(input())

    while True:
        branches = input().split(" ")

        if branches[0] == "-1":
            break

        father = int(branches[0])

        if not father in fathers:
            fathers[father] = None

        for i in range(1, len(branches)):
            fathers[int(branches[i])] = father
    
    path = []

    d = kitten_node

    while d != None:
        path.append(d)
        d = fathers[d]

    for node in path:
        print(node, end = ' ')

main()