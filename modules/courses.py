def get_course(num):
    """
    :param num: number to identify the course
    :return: name of the course based on the given number
    """

    try:
        num = int(num)
    except ValueError:
        num = -1

    match num:
        case -1:
            return "CastingError"
        case 33 | 9556:
            """Used to be 33 - Biofuel Production Technologies and 9556 - Oral Hygiene
               Becuase it is not that much, it will be counted as Others"""
            return "Other"
        case 171:
            return "Animation and Multimedia Design"
        case 8014 | 9238:
            """The data separates this course to a 'normal' and an evening course. 
               This will be ignored in this case"""
            return "Social Service"
        case 9003:
            return "Agronomy"
        case 9070:
            return "Communication Design"
        case 9085:
            return "Veterinary Nursing"
        case 9119:
            return "Informatics Engineering"
        case 9130:
            return "Equinculture"
        case 9147 | 9991:
            """The data separates this course to a 'normal' and an evening course. 
               This will be ignored in this case"""
            return "Management"
        case 9254:
            return "Tourism"
        case 9500:
            return "Nursing"
        case 9670:
            return "Advertising and Marketing Management"
        case 9773:
            return "Journalism and Communication"
        case 9853:
            return "Basic Education"
        case _:
            return "Unknown course number"
