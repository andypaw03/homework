with open('mem.txt', 'w') as file:
    for i in range(1, 1000, 2):
        file.write(str(i)+"\n")