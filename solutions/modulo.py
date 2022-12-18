# https://open.kattis.com/problems/modulo

def main():

    i = 0
    m = []

    while i < 10:

        n = int(input())

        if n % 42 not in m:
            m.append(n % 42)
        i += 1

    print(len(m))

main()