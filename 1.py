numbers = [str(i) for i in range(10)]
with open("input_1.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for l in lines:
        number = ''.join([i for i in l if i in numbers])
        number = int(number[0] + number[-1])
        sum += number
    print(sum)