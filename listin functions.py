def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5,4,3]))

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

def is_year_leap(year):
    # Write your code here.
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False



test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")



def is_leap_year(year):
    """Check if a given year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """Return the number of days in a given month of a specific year."""
    if not isinstance(year, int) or not isinstance(month, int):
        return None  # Ensure both inputs are integers
    if year < 1 or month < 1 or month > 12:
        return None  # Ensure valid year and month range
    
    month_lengths = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    return month_lengths[month - 1]

# Testing the function
test_cases = [
    (2024, 2, 29),  # Leap year February
    (2023, 2, 28),  # Non-leap year February
    (2000, 2, 29),  # Leap year divisible by 400
    (1900, 2, 28),  # Not a leap year (divisible by 100 but not 400)
    (2022, 4, 30),  # April has 30 days
    (2022, 7, 31),  # July has 31 days
    (-100, 2, None),  # Invalid year
    (2024, 0, None),  # Invalid month
    (2024, 13, None),  # Invalid month
    (2024, 'February', None),  # Invalid type
    ('year', 2, None),  # Invalid type
]

for year, month, expected in test_cases:
    result = days_in_month(year, month)
    print(f"days_in_month({year}, {month}) = {result}, expected = {expected}")
    assert result == expected, f"Test failed for year={year}, month={month}"

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))


