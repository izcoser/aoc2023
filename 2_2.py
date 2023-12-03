colors = ["red", "blue", "green"]

with open("input_2.txt", "r") as f:
    lines = f.readlines()
    sum = 0

    for l in lines:
        min_red = min_blue = min_green = 0
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

                if (color == "red" and number > min_red):
                    min_red = number
                
                if (color == "green" and number > min_green):
                    min_green = number
                
                if (color == "blue" and number > min_blue):
                    min_blue = number
        
        sum += (min_red * min_green * min_blue)
    print(sum)