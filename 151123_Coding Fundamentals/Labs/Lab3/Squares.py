start_num = 1
while (start_num >= 1 and start_num < 100):
    print(start_num)
    start_num_squared = start_num ** 2
    print(start_num_squared)
    start_num = start_num + 1
    if start_num_squared > 2000:
        break