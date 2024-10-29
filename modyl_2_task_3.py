my_list = [42, 69, 322, 13, 0, -5, 99, 9, 8, 7, -6, 5]
print(len(my_list))

counter = 0
while True:
    if counter >= len(my_list):
        break

    value = my_list[counter]
    if value >= 0:
        print(2)
    else:
        print(3)

    counter += 1  


