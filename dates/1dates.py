# 1.- Friday the 13th

def has_friday_13(month:int, year:int, day:int = 13) -> bool:
    """Function that receives month and year as a parameters
    and returns True if that month has a friday 13, and false
    if not

    Args:
        month (int): month to review if has a friday 13
        year (int): year to review
        day (int, optional): _description_. Defaults to 13.

    Returns:
        bool: True if the month has 13, false if not
    """
    import datetime
    weekDays:list = ["Monday","Tuesday","Wednesday","Thursday","Friday", 
                    "Saturday", "Sunday"]
    thirteen_date = datetime.date(year,month,day)
    thirteen_date_day:int = thirteen_date.weekday()
    return True if weekDays[thirteen_date_day] == "Friday" else False
# TESTS:    
# print(has_friday_13(3, 2020))
# print(has_friday_13(10, 2017))
# print(has_friday_13(8, 2024))

