from datetime import datetime, date
import holidays

def today():    
    us_holidays = holidays.US(years=range(2025, 2026))
    todays_date = date.today()
    next_holiday = us_holidays.get_closest_holiday(todays_date)

    return f"The next closest holiday is {next_holiday[1]} on the date: {next_holiday[0]}"

if __name__=="__main__":
    print(today())