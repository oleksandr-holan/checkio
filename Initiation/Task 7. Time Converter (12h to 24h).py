def time_converter(time):

    # if time[:-8] == '12':
    #     time = '00' + time[-8:]
    # if time[-4:] == 'p.m.':
    #     time = f'{int(time[:-8]) + 12}{time[-8:-5]}'
    # else:
    #     time = time[:-5]
    # return f'{time:0>5}'
    return f'{int(time[:-8]) % 12 + 12 * ("p" in time):0>2}{time[-8:-5]}'


if __name__ == "__main__":
    print("Example:")
    print(time_converter("12:30 p.m."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter("12:30 p.m.") == "12:30"
    print(time_converter("9:00 a.m."))
    assert time_converter("9:00 a.m.") == "09:00"
    assert time_converter("11:15 p.m.") == "23:15"
    print(time_converter("6:50 p.m."))
    assert time_converter("6:50 p.m.") == "18:50"
    print(time_converter("12:00 a.m."))
    print("Coding complete? Click 'Check' to earn cool rewards!")
