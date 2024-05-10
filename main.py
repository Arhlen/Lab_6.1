with open('data.csv') as file:
    file.readline()
    count_do_30_0 = 0
    count_do_30_all = 0
    count_60_0 = 0
    count_60_all = 0
    for line in file.readlines():
        data = line.split(',')
        if data[1] == '' or data[6] == '':
            continue
        survived = data[1]
        age = float(data[6])
        if age <= 30:
            count_do_30_all += 1
            if survived == '0':
                count_do_30_0 += 1
        if age >= 60:
            count_60_all += 1
            if survived == '0':
                count_60_0 += 1
    print('Доляпогибшихвгруппедо 30 лет:', count_do_30_0 / count_do_30_all)
    print('Доляпогибшихвгруппестарше 60 лет:', count_60_0 / count_60_all)
