def main():

    n = int(input())

    prices = []

    for i in range(n):
        prices.append(int(input()))
    
    prices.sort(reverse = True)

    minimum = 0

    for i in range(n):
        if (i + 1) % 3 != 0:
            minimum += prices[i]

    print(minimum)

main()