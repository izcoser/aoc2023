colors = ["red", "blue", "green"]

with open("input_2.txt", "r") as f:
    lines = f.readlines()
    sum = 0


    for l in lines:
        game_possible = True
        game_id = int(l.split(":")[0].split()[1])
        rounds = l.split(":")[1].split(";")
        for r in rounds:
            shows = [s.strip() for s in r.split(",")]
            for s in shows:
                s_copy = s
                color = ''
                for i in colors:
                    if i in s_copy:
                        color = i
                        s_copy = s_copy.replace(" " + i, "")

                number = int(s_copy)
                assert color != ''

                if (color == "red" and number > 12) or (color == "green" and number > 13) or (color == "blue" and number > 14):
                    game_possible = False
        
        if game_possible:
            sum += game_id
    print(sum)