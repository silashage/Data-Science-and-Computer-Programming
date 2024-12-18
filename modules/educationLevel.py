def get_parents_education_level(num):
    """
    :param num: number for the education_level identification
    :return: education level based on the given number
    """

    try:
        num = int(num)
    except ValueError:
        num = -1

    match num:
        case -1:
            return "CastingError"
        case 1:
            return "Secondary Education - 12th Year of Schooling"
        case 2 | 3 | 4 | 5:
            """Includes Bachelor, Master, unspecified Degree and Doctor Degree"""
            return "Higher Education - Degree"
        case 6:
            return "Frequency of Higher Education"
        case 9:
            return "12th Year of Schooling - Not Completed"
        case 10:
            return "11th Year of Schooling - Not Completed"
        case 11:
            return "7th Year (Old)"
        case 12:
            return "Other - 11th Year of Schooling"
        case 13:
            return "2nd year complementary high school course"
        case 14:
            return "10th Year of Schooling"
        case 18:
            return "General commerce course"
        case 19:
            return "Basic Education (9th/10th/11th Y.)"
        case 20:
            return "Complementary High School Course"
        case 22:
            return "Technical-professional course"
        case 25:
            return "Complementary High School Course - not concluded"
        case 26:
            return "7th year of schooling"
        case 27:
            return "2nd cycle of the general high school course"
        case 29:
            return "9th Year of Schooling - Not Completed"
        case 30:
            return "8th year of schooling"
        case 31:
            return "General Course of Administration and Commerce"
        case 33:
            return "Supplementary Accounting and Administration"
        case 34:
            return "Unknown"
        case 35:
            return "Can't read or write"
        case 36:
            return "Can read without having a 4th year of schooling"
        case 37:
            return "Basic education (4th/5th Y.)"
        case 38:
            return "Basic Education (6th/7th/8th Y.)"
        case 39:
            return "Technological specialization course"
        case 40:
            return "Higher education - degree (1st cycle)"
        case 41:
            return "Specialized higher studies course"
        case 42:
            return "Professional higher technical course"
        case 43:
            return "Higher Education - Master (2nd cycle)"
        case 44:
            return "Higher Education - Doctorate (3rd cycle)"
        case _:
            return "Unknown education level"
