from data import oscar_data


def filter_by_year(data, begin, end):
    result = []
    for row in data:
        year = row[1]
        if begin <= year < end:
            result.append(row)
    return result

def column_sum(data, column):
    result = 0
    for row in data:
        result += row[column]
    return result

def column_mean(data, column):
    total = column_sum(data, column)
    mean = total / len(data)
    return mean

def add_price_per_minute(data):
    for i in range(len(data)):
        length = data[i][3]
        budget = data[i][5]
        price_per_minute = budget / length
        data[i].append(price_per_minute)

def do_research():
    add_price_per_minute(oscar_data)

    years = [[1988, 1998], [1998, 2008], [2008, 2018]]

    rows = []
    for begin_end in years:
        begin = begin_end[0]
        end = begin_end[1]

        name = '{}-{}'.format(begin, end)

        filter_data = filter_by_year(oscar_data, begin, end)

        mean_score = column_mean(filter_data, 2)
        mean_length = column_mean(filter_data, 3)
        mean_ppm = column_mean(filter_data, 7)
        mean_gross = column_mean(filter_data, 6)

        rows.append([name, mean_score, mean_length, mean_ppm, mean_gross])

    print('Годы      | Рейтинг | Длина  | Бюджет за минуту | Сборы ')
    print('--------------------------------------------------------')
    for row in rows:
        print('{: <9} | {: >7.2f} | {: >5.2f} | {: >16.2f} | {: >6.2f}'.format(
            row[0], row[1], row[2], row[3], row[4]))
