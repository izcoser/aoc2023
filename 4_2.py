with open("input_4.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    total_cards = { i: 1 for i in range(len(lines))}
    s = 0
    for index, l in enumerate(lines):
        winning = [int(i) for i in l.split("|")[0].split(":")[1].strip().split()]
        numbers = [int(i) for i in l.split("|")[1].strip().split()]
        score = sum([1 if i in winning else 0 for i in numbers])
        
        for i in range(score):
            total_cards[index + i + 1] += total_cards[index]


        print(score)

    total = sum(total_cards.values())
    print(total)