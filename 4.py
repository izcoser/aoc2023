with open("input_4.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    s = 0
    for l in lines:
        winning = [int(i) for i in l.split("|")[0].split(":")[1].strip().split()]
        numbers = [int(i) for i in l.split("|")[1].strip().split()]
        score = 2 ** (sum([1 if i in winning else 0 for i in numbers]) - 1)
        s += score if score >= 1 else 0
        print(score)

    print(s)