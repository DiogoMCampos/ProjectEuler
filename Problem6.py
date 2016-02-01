def problem6():
    diff = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if j > i:
                diff += 2 * i * j

    print(diff)

problem6()
