def is_weekend(weekday_number):
    return weekday_number < 8 and weekday_number in range(6, 8)


def get_discount(total_purchase):
    return total_purchase / 10 if total_purchase >= 5000 else \
        total_purchase / 20 if total_purchase >= 1000 else 0


def describe_number(input_number):
    parity = 'чётное' if input_number % 2 == 0 else 'нечётное'
    digit_count = 'однозначное' if len(str(input_number)) == 1 else \
                 'двузначное' if len(str(input_number)) == 2 else \
                 'трёхзначное'
    return f"{parity} {digit_count} число"


def convert_to_meters(unit_type, measurement):
    match unit_type:
        case 1:
            return measurement / 10
        case 2:
            return measurement * 1000
        case 3:
            return measurement
        case 4:
            return measurement / 1000
        case 5:
            return measurement / 100
        case _:
            return 0


def describe_age(years_old):
    digit_words = {
        1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
        5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
    }
    tens_words = {
        2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
        6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'
    }

    if years_old == 100:
        age_text = 'сто'
    else:
        tens = years_old // 10
        units = years_old % 10
        age_text = tens_words[tens]
        if units != 0:
            age_text += ' ' + digit_words[units]

    last_digit = years_old % 10
    if last_digit == 1:
        age_unit = 'год'
    elif 2 <= last_digit <= 4:
        age_unit = 'года'
    else:
        age_unit = 'лет'

    return f"{age_text} {age_unit}"