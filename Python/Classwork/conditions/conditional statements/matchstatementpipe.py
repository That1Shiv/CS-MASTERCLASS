# This match statement uses the pipe symbol to combine cases, letting you match multiple values in a single case for cleaner code.
day = 6
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("today is not a weekend")
    case 6 | 7:
        print("today is a weekend")
    case _:
        print("looking forward to next week")
