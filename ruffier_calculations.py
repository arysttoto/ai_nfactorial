def result_comments(result, age):
    if age in range(7, 9):
        if result<6.5:
            value = 10
            return value
        elif result>=6.5 and result<12:
            value = 8
            return value
        elif result>=12 and result<17:
            value = 6
            return value
        elif result>=17 and result<21:
            value = 4
            return value
        elif result>=21:
            value = 2
            return value
    elif age in range(9, 11):
        if result<5:
            value = 10
            return value
        elif result>=5 and result<10.5:
            value = 8
            return value
        elif result>=10.5 and result<15.5:
            value = 6
            return value
        elif result>=15.5 and result<19.5:
            value = 4
            return value
        elif result>=19.5:
            value = 2
            return value
    elif age in range(11, 13):
        if result<3.5:
            value = 10
            return value
        elif result>=3.5 and result<9:
            value = 8
            return value
        elif result>=9 and result<14:
            value = 6
            return value
        elif result>=14 and result<18:
            value = 4
            return value
        elif result>=18:
            value = 2
            return value
    elif age in range(13, 15):
        if result < 2:
            value = 10
            return value
        elif result >= 2 and result < 7.5:
            value = 8
            return value
        elif result >= 7.5 and result < 12.5:
            value = 6
            return value
        elif result >= 12.5 and result < 16.5:
            value = 4
            return value
        elif result >= 16.5:
            value = 2
            return value
    elif age>=15:
        if result<0.5:
            value = 10
            return value
        elif result>=0.5 and result<6:
            value = 8
            return value
        elif result>=6 and result<11:
            value = 6
            return value
        elif result>=11 and result<15:
            value = 4
            return value
        elif result>=15:
            value = 2
            return value