def source_to_destination(s_value: int, map: list[int]) -> int:
    for destination_start, source_start, rrange in map:
        if s_value >= source_start and s_value < source_start + rrange:
            shift = s_value - source_start
            return destination_start + shift
    return s_value

with open("input_5.txt") as f:
    lines = [i.strip() for i in f.readlines()]
    seeds = [int(i) for i in lines[0].split(":")[1].split()]

    maps = []
    for line in lines[1:]:
        if line == '':
            continue

        if "map:" in line:
            maps.append([])
            continue

        destination_start, source_start, rrange = [int(i) for i in line.split()]
        maps[len(maps) - 1].append((destination_start, source_start, rrange))

    
    lowest_location = -1
    for s in seeds:
        destination = s
        for map in maps:
            destination = source_to_destination(destination, map)
        if (destination < lowest_location) or lowest_location == -1:
            lowest_location = destination

    print(lowest_location)