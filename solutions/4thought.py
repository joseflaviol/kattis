def main():
    x = ["4 + 4", "4 - 4", "4 * 4", "4 // 4"]
    y = [" + ", " - " , " * ", " // "]

    d = {}

    for exp in x:
        for op in y:
            for e in x:
                s = exp + op + e
                ev = eval(s)
                s = s.replace("//", "/")
                d[ev] = s
    
    n = int(input())

    for i in range(n):
        q = int(input())

        if q in d.keys():
            print("%s = %d" % (d[q], q))
        else:
            print("no solution")

main()