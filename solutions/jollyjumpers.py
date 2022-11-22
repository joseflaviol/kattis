def main():

    while True:
        try:
            l = input().split(" ")

            n = int(l[0])

            seq = []

            for i in range(1, n):
                seq.append(i)

            numbers = []

            for i in range(1, len(l)):
                numbers.append(int(l[i]))

            for i in range(0, len(numbers) - 1):
                c = abs(numbers[i] - numbers[i + 1])
                if not(0 < c < n):
                    break 
                else:
                    if c in seq:
                        seq.remove(c)

            if len(seq) == 0:
                print("Jolly")
            else:
                print("Not jolly")    
    
        except EOFError:
            break

main()