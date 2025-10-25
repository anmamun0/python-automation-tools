import calendar

def display_calendar(year, month):
    # Create a calendar
    cal = calendar.monthcalendar(year, month)

    # Get the month name
    month_name = calendar.month_name[month]

    # Print the calendar
    print(f"{month_name} {year}")
    print("Mo Tu We Th Fr Sa Su")
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end="")
            else:
                print(f"{day:2} ", end="")
        print()

# Test the program
year = 2022
month = 2
display_calendar(year, month)
