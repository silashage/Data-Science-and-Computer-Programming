def get_country(num):
    """
    :param num: number to identify the country
    :return: name of the country based on the given number
    """

    try:
        num = int(num)
    except ValueError:
        num = -1

    match num:
        case -1:
            return "CastingError"
        case 1:
            return "Portuguese"
        case 2:
            return "German"
        case 6:
            return "Spanish"
        case 11:
            return "Italian"
        case 13:
            return "Dutch"
        case 14:
            return "English"
        case 17:
            return "Lithuanian"
        case 21:
            return "Angolan"
        case 22:
            return "Cape Verdean"
        case 24:
            return "Guinean"
        case 25:
            return "Mozambican"
        case 26:
            return "Santomean"
        case 32:
            return "Turkish"
        case 41:
            return "Brazilian"
        case 62:
            return "Romanian"
        case 100:
            return "Moldova (Republic of)"
        case 101:
            return "Mexican"
        case 103:
            return "Ukrainian"
        case 105:
            return "Russian"
        case 108:
            return "Cuban"
        case 109:
            return "Colombian"
        case _:
            return "UNKNOWN"
