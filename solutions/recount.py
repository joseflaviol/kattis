def main():

    votes = {}

    while True:

        candidate = input()

        if candidate == "***":
            break

        if not candidate in votes:
            votes[candidate] = 1
        else:
            votes[candidate] += 1
 
    winner = max(votes, key = votes.get)

    for key in votes.keys():
        if votes[winner] == votes[key] and key != winner:
            winner = "Runoff!"
            break 
    
    print(winner)

main()