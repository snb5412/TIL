with open('number.txt', 'r') as f:
    lines = f.readlines()

    with open('number.txt', 'w') as f:
        for i in range(len(lines)):
            f.write(lines[-1 * (i+1)])

# list.reverse() : list 뒤집기