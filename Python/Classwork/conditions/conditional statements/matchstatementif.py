# This match statement uses conditions with cases, allowing you to match values only when an additional condition is met.
month = 5
day = 4 
match day: 
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("today is a weekday in april")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("today is a weekday in may")
    case _:
        print("no match")
