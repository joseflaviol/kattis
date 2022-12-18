# https://open.kattis.com/problems/okviri

def main():

    shape = ["..#..", ".#.#.", "#.0.#", ".#.#.", "..#.."]

    word = input()

    s = ""
    for i in range(5):
        aux = shape[i]
        
        for j in range(len(word)):
            if (j + 1) % 3 == 0:
                aux = aux.replace("#", "*")
            elif j != 0 and (j + 1) % 3 == 1:
                aux = aux[1:len(aux)]
            
            if j + 1 < len(word) and (j + 1) % 3 != 0:
                aux = aux[0:len(aux) - 1]
            if (i == 2):
                aux = aux.replace("0", word[j])    
            s += aux 
            aux = shape[i]
        s += "\n"
    
    print(s)

main()