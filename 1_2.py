numbers = [str(i) for i in range(10)]
numbers2 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def written_number_in_string(s: str):
    for n in numbers2:
        if n in s:
            return True, str(numbers2.index(n))
    return False, -1

def find_number(s: str):
    first = -1
    second = -1
    partial = ''
    for c in s:
        if c in numbers:
            first = c
            break
        
        partial += c
        found, n = written_number_in_string(partial)
        if found:
            first = n
            break
    
    partial = ''
    for c in s[::-1]:
        if c in numbers:
            second = c
            break

        partial += c
        found, n = written_number_in_string(partial[::-1])
        if found:
            second = n
            break
        
    assert first != -1
    assert second != -1
    return int(first + second)


with open("input_1.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for l in lines:
        n = find_number(l)
        sum += n
    print(sum)
